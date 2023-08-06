from celery import states
from games.models import GameSystem, GameCollection

from django_celery_results.models import TaskResult

IN_PROGRESS_STATES = [states.PENDING, states.STARTED, states.RETRY]


def game_systems(request):
    return {
        "game_systems": GameSystem.objects.all(),
        "game_collections": GameCollection.objects.all(),
        "update_in_progress": TaskResult.objects.filter(
            task_name="games.tasks.update_roms",
            status__in=IN_PROGRESS_STATES,
        ),
    }
