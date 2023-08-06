import json
import logging
from datetime import datetime

from celery import states
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.db.models import Avg, Count, F
from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from django.views.generic.list import MultipleObjectMixin
from django_celery_results.models import TaskResult

from games.tasks import update_roms

from .models import Developer, Game, GameCollection, GameSystem, Genre, Publisher

logger = logging.Logger(__name__)


IN_PROGRESS_STATES = [states.PENDING, states.STARTED, states.RETRY]


class RecentGameList(ListView):
    model = Game
    paginate_by = 10
    queryset = Game.objects.order_by("-created")[:70]

    def get_context_data(self, **kwargs):
        cached_game_id = cache.get("todays_game_id", None)
        if not cached_game_id:
            todays_game = (
                Game.objects.filter(rating__gte=settings.FEATURED_THRESHOLD, featured_on__isnull=True)
                .order_by("?")
                .first()
            )
            featured_collection = GameCollection.objects.filter(
                slug="emus-featured"
            ).first()
            if featured_collection:
                featured_collection.games.add(todays_game)
                featured_collection.save()
            cache.set("todays_game_id", todays_game.id, settings.FEATURED_GAME_DURATION)
            todays_game.featured_on = datetime.now()
            todays_game.save(update_fields=["featured_on"])
        else:
            todays_game = Game.objects.get(id=cached_game_id)

        return super(RecentGameList, self).get_context_data(
            todays_game=todays_game,
            **kwargs,
        )


class LibraryGameList(ListView):
    template_name = "games/game_library_list.html"
    model = Game
    paginate_by = 400
    default_sort_key = "-created"

    def get_context_data(self, **kwargs):
        game_system_slug = self.request.GET.get("game_system")
        order_by = self.request.GET.get("order_by", self.default_sort_key)
        if order_by[0] == "-":
            order_by = order_by[1:]
            object_list = Game.objects.order_by(F(order_by).desc(nulls_last=True))
        else:
            object_list = Game.objects.order_by(F(order_by).asc(nulls_last=True))
        if game_system_slug:
            object_list = object_list.filter(
                game_system__retropie_slug=game_system_slug
            )
        context = super(LibraryGameList, self).get_context_data(
            object_list=object_list, **kwargs
        )
        return context


class FilterableBaseListView(ListView):
    def get_queryset(self, **kwargs):
        order_by = self.request.GET.get("order_by", "name")
        queryset = super().get_queryset(**kwargs)
        queryset = queryset.annotate(num_games=Count("game")).annotate(
            rating=Avg("game__rating")
        )

        if order_by[0] == "-":
            order_by = order_by[1:]
            queryset = queryset.order_by(F(order_by).desc(nulls_last=True))
        else:
            queryset = queryset.order_by(F(order_by).asc(nulls_last=True))
        return queryset


class PublisherList(FilterableBaseListView):
    model = Publisher


class DeveloperList(FilterableBaseListView):
    model = Developer


class GenreList(FilterableBaseListView):
    model = Genre


class GameDetail(DetailView):
    model = Game


class GamePlayDetail(DetailView, LoginRequiredMixin):
    template_name = "games/game_play_detail.html"
    model = Game


class GameSystemList(ListView):
    model = GameSystem


class GameSystemDetail(DetailView, MultipleObjectMixin):
    model = GameSystem
    paginate_by = 20

    def get_context_data(self, **kwargs):
        object_list = Game.objects.filter(game_system=self.get_object())
        context = super(GameSystemDetail, self).get_context_data(
            object_list=object_list, **kwargs
        )
        return context


class GenreDetail(DetailView, MultipleObjectMixin):
    model = Genre
    paginate_by = 20

    def get_context_data(self, **kwargs):
        object_list = Game.objects.filter(genre=self.get_object())
        context = super(GenreDetail, self).get_context_data(
            object_list=object_list, **kwargs
        )
        return context


class PublisherDetail(DetailView, MultipleObjectMixin):
    model = Publisher
    paginate_by = 20

    def get_context_data(self, **kwargs):
        object_list = Game.objects.filter(publisher=self.get_object())
        context = super(PublisherDetail, self).get_context_data(
            object_list=object_list, **kwargs
        )
        return context


class DeveloperDetail(DetailView, MultipleObjectMixin):
    model = Developer
    paginate_by = 20

    def get_context_data(self, **kwargs):
        object_list = Game.objects.filter(developer=self.get_object())
        context = super(DeveloperDetail, self).get_context_data(
            object_list=object_list, **kwargs
        )
        return context


class GameCollectionList(ListView):
    model = GameCollection


class GameCollectionDetail(DetailView, LoginRequiredMixin):
    model = GameCollection

    def get_context_data(self, **kwargs):
        collection = self.get_object()
        order_by = self.request.GET.get("order_by", "release_date")
        object_list = collection.games.all()

        if order_by[0] == "-":
            order_by = order_by[1:]
            object_list = object_list.order_by(F(order_by).desc(nulls_last=True))
        else:
            object_list = object_list.order_by(F(order_by).asc(nulls_last=True))

        context = super(GameCollectionDetail, self).get_context_data(
            object_list=object_list, **kwargs
        )
        return context


@login_required
def trigger_rom_update(request):
    full_scan = request.GET.get("full_scan", False)
    if full_scan == "true":
        full_scan = True

    game_systems = request.GET.getlist("game_systems")
    if not game_systems:
        game_systems = list(settings.GAME_SYSTEM_DEFAULTS.keys())

    try:
        update_roms.delay(game_systems, full_scan=full_scan)
    except FileNotFoundError:
        return HttpResponse(
            json.dumps({"success": False, "msg": "Skyscraper is not installed"}),
            status=400,
            content_type="application/json",
        )
    return HttpResponse(
        json.dumps({"success": True, "msg": "Library scan started"}),
        status=200,
        content_type="application/json",
    )


@login_required
def library_update_status(request):
    update_task = TaskResult.objects.filter(
        task_name="games.tasks.update_roms",
        status__in=IN_PROGRESS_STATES,
    ).first()

    if not update_task:
        state = states.SUCCESS
    else:
        state = update_task.status

    return HttpResponse(
        json.dumps({"state": state}),
        status=200,
        content_type="application/json",
    )
