from django.contrib import admin

from games.models import Developer, Game, GameSystem, Genre, Publisher, GameCollection


class GameAdmin(admin.ModelAdmin):
    date_hierarchy = "created"
    list_display = ("name", "game_system", "rating", "region", "featured_on",)
    list_filter = (
        "undub",
        "english_patched",
        "hack",
        "region",
        "game_system",
        "featured_on",
    )
    ordering = ("-created",)
    search_fields = [
        "name",
        "description",
        "region",
    ]


class GameInline(admin.TabularInline):
    model = Game


class GameCollectionAdmin(admin.ModelAdmin):
    filter_horizontal = ("games",)
    raw_id_fields = (
        "developer",
        "publisher",
        "genre",
        "game_system",
    )


admin.site.register(GameCollection, GameCollectionAdmin)
admin.site.register(GameSystem)
admin.site.register(Developer)
admin.site.register(Publisher)
admin.site.register(Genre)
admin.site.register(Game, GameAdmin)
