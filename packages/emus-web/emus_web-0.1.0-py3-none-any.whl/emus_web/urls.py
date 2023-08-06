from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from games import urls as games_urls
from search import urls as search_urls
from games.views import RecentGameList
from games.api.views import (
    DeveloperViewSet,
    GameSystemViewSet,
    GameViewSet,
    GameCollectionViewSet,
    PublisherViewSet,
    GenreViewSet,
)
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"games", GameViewSet)
router.register(r"publishers", PublisherViewSet)
router.register(r"developers", DeveloperViewSet)
router.register(r"genre", GenreViewSet)
router.register(r"game-systems", GameSystemViewSet)
router.register(r"game-collections", GameCollectionViewSet)

urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api/v1/", include(router.urls)),
    path("search/", include(search_urls, namespace="search")),
    path("games/", include(games_urls, namespace="games")),
    path("", RecentGameList.as_view(), name="home"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
