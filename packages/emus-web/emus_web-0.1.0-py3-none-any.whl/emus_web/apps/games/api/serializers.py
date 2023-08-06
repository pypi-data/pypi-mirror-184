from games.models import Developer, Game, GameSystem, Genre, Publisher, GameCollection
from rest_framework import serializers


class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'
        extra_fields = ['id']


class DeveloperSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Developer
        fields = (
            "id",
            "name",
            "slug",
        )


class PublisherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Publisher
        fields = (
            "id",
            "name",
            "slug",
        )


class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genre
        fields = (
            "id",
            "name",
            "slug",
        )


class GameSystemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GameSystem
        fields = (
            "id",
            "name",
            "retropie_slug",
            "slug",
        )

class GameCollectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GameCollection
        fields = (
            "id",
            "name",
            "slug",
            "games",
        )
