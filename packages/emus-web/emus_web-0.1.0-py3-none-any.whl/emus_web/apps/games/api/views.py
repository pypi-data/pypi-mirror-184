from games.api.serializers import (
    DeveloperSerializer,
    GameSerializer,
    GameSystemSerializer,
    GenreSerializer,
    PublisherSerializer,
    GameCollectionSerializer,
)
from django_filters.rest_framework import DjangoFilterBackend
from games.models import Developer, Game, GameSystem, Genre, Publisher, GameCollection
from rest_framework import viewsets


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['rating', 'english_patched', "undub", "kid_game","region", "hack"]


class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class DeveloperViewSet(viewsets.ModelViewSet):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GameSystemViewSet(viewsets.ModelViewSet):
    queryset = GameSystem.objects.all()
    serializer_class = GameSystemSerializer


class GameCollectionViewSet(viewsets.ModelViewSet):
    queryset = GameCollection.objects.all()
    serializer_class = GameCollectionSerializer


