from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render
from games.models import Game


@login_required
def search(request):
    results = []
    query = ""
    if request.method == "GET":
        query = request.GET.get("q")
        if not query:
            return render(
                request,
                "search/search.html",
                {"query": query, "results": results},
            )

        results = Game.objects.filter(
            Q(name__icontains=query)
            | Q(game_system__name__icontains=query)
            | Q(publisher__name__icontains=query)
            | Q(genre__name__icontains=query)
            | Q(publisher__name__icontains=query)
            | Q(developer__name__icontains=query)
        ).distinct()
    return render(
        request, "search/search.html", {"query": query, "results": results}
    )
