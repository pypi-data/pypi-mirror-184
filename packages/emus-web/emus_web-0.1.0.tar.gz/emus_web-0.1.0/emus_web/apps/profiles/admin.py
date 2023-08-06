from profiles.models import (
    UserGamePlaythrough,
    UserGamePlaythroughUpdate,
    UserProfile,
)
from django.contrib import admin


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    filter_horizontal = ("favorite_games",)


@admin.register(UserGamePlaythrough)
class UserGamePlaythroughAdmin(admin.ModelAdmin):
    raw_id_fields = ["game"]


@admin.register(UserGamePlaythroughUpdate)
class UserGamePlaythroughUpdateAdmin(admin.ModelAdmin):
    ...
