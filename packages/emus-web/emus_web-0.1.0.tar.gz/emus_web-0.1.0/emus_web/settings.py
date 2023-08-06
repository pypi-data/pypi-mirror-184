import os
import sys
from pathlib import Path

import dj_database_url
from django.utils.translation import gettext_lazy as _
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))


# Tap emus.conf if it's available
if os.path.exists("emus.conf"):
    load_dotenv("emus.conf")
elif os.path.exists("/etc/emus.conf"):
    load_dotenv("/etc/emus.conf")
elif os.path.exists("/usr/local/etc/emus.conf"):
    load_dotenv("/usr/local/etc/emus.conf")

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("EMUS_SECRET_KEY", "not-a-secret-234lkjasdflj132")


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("EMUS_DEBUG", False)

TESTING = len(sys.argv) > 1 and sys.argv[1] == "test"

FEATURED_GAME_DURATION = os.getenv("EMUS_FEATURED_GAME_DURATION", 60 * 60 * 18)

ALLOWED_HOSTS = ["*"]
CSRF_TRUSTED_ORIGINS = [
    os.getenv("EMUS_TRUSTED_ORIGINS", "http://localhost:8000")
]
X_FRAME_OPTIONS = "SAMEORIGIN"

REDIS_URL = os.getenv("EMUS_REDIS_URL", None)

CELERY_TASK_ALWAYS_EAGER = os.getenv("EMUS_SKIP_CELERY", False)
CELERY_BROKER_URL = REDIS_URL if REDIS_URL else "memory://localhost/"
CELERY_RESULT_BACKEND = "django-db"
CELERY_TIMEZONE = os.getenv("EMUS_TIME_ZONE", "EST")
CELERY_TASK_TRACK_STARTED = True

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django_filters",
    "django_extensions",
    "markdownify.apps.MarkdownifyConfig",
    "taggit",
    "profiles",
    "mathfilters",
    "search",
    "games",
    "rest_framework",
    "allauth",
    "allauth.account",
    "django_celery_results",
    "simple_history",
]

SITE_ID = 1

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.gzip.GZipMiddleware",
    "simple_history.middleware.HistoryRequestMiddleware",
]

ROOT_URLCONF = "emus_web.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [str(PROJECT_ROOT.joinpath("templates"))],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "games.context_processors.game_systems",
            ],
        },
    },
]

WSGI_APPLICATION = "emus_web.wsgi.application"

DATABASES = {
    "default": dj_database_url.config(
        default=os.getenv("EMUS_DATABASE_URL", "sqlite:///db.sqlite3"),
        conn_max_age=600,
    ),
}
if TESTING:
    DATABASES = {
        "default": dj_database_url.config(default="sqlite:///testdb.sqlite3")
    }


CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "unique-snowflake",
    }
}
if REDIS_URL:
    CACHES["default"][
        "BACKEND"
    ] = "django.core.cache.backends.redis.RedisCache"
    CACHES["default"]["LOCATION"] = REDIS_URL

SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticated",
    ),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend"
    ],
    "PAGE_SIZE": 100,
}

LOGIN_REDIRECT_URL = "/"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = os.getenv("EMUS_TIME_ZONE", "EST")

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = os.getenv("EMUS_STATIC_ROOT", os.path.join(BASE_DIR, "static"))

MEDIA_URL = "/media/"
MEDIA_ROOT = os.getenv("EMUS_MEDIA_ROOT", os.path.join(BASE_DIR, "media"))
ROMS_DIR = os.path.join(MEDIA_ROOT, "roms")
COLLECTIONS_DIR = os.path.join(ROMS_DIR, "emulationstation-collections")

SCRAPER_BIN_PATH = os.getenv("EMUS_SCRAPER_BINPATH", "Skyscraper")
SCRAPER_CONFIG_FILE = os.getenv("EMUS_SCRAPER_CONFIG_FILE", "skyscraper.ini")
SCRAPER_SITE = os.getenv("EMUS_SCRAPER_SITE", "screenscraper")
SCRAPER_FRONTEND = os.getenv("EMUS_FRONTEND", "emulationstation")

JSON_LOGGING = os.getenv("EMUS_JSON_LOGGING", False)
LOG_TYPE = "json" if JSON_LOGGING else "log"

FEATURED_THRESHOLD = os.getenv("EMUS_FEATURED_THRESHOLD", 0.80)
default_level = "INFO"
if DEBUG:
    default_level = "DEBUG"

LOG_LEVEL = os.getenv("EMUS_LOG_LEVEL", default_level)
LOG_FILE_PATH = os.getenv("EMUS_LOG_FILE_PATH", "/tmp/")

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "root": {
        "handlers": ["console", "file"],
        "level": LOG_LEVEL,
        "propagate": True,
    },
    "formatters": {
        "color": {
            "()": "colorlog.ColoredFormatter",
            # \r returns caret to line beginning, in tests this eats the silly dot that removes
            # the beautiful alignment produced below
            "format": "\r"
            "{log_color}{levelname:8s}{reset} "
            "{bold_cyan}{name}{reset}:"
            "{fg_bold_red}{lineno}{reset} "
            "{thin_yellow}{funcName} "
            "{thin_white}{message}"
            "{reset}",
            "style": "{",
        },
        "log": {"format": "%(asctime)s %(levelname)s %(message)s"},
        "json": {
            "()": "pythonjsonlogger.jsonlogger.JsonFormatter",
            "format": "%(levelname)s %(name) %(funcName) %(lineno) %(asctime)s %(message)s",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "color",
            "level": LOG_LEVEL,
        },
        "null": {
            "class": "logging.NullHandler",
            "level": LOG_LEVEL,
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": "".join([LOG_FILE_PATH, "emus.log"]),
            "formatter": LOG_TYPE,
            "level": LOG_LEVEL,
        },
        "requests_file": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": "".join([LOG_FILE_PATH, "emus_requests.log"]),
            "formatter": LOG_TYPE,
            "level": LOG_LEVEL,
        },
    },
    "loggers": {
        # Quiet down our console a little
        "django": {
            "handlers": ["file"],
            "propagate": True,
        },
        "django.db.backends": {"handlers": ["null"]},
        "emus_web": {
            "handlers": ["console", "file"],
            "propagate": True,
        },
    },
}

REMOVE_FROM_SLUGS = ["_", " ", "/"]

if DEBUG:
    # We clear out a db with lots of games all the time in dev
    DATA_UPLOAD_MAX_NUMBER_FIELDS = 3000

GAME_SYSTEM_DEFAULTS = {
    "3do": {
        "name": "3DO",
        "retroarch_core": "opera",
    },
    "3ds": {
        "name": "Nintendo 3DS",
        "retroarch_core": "citra",
    },
    "atari2600": {
        "name": "Atari 2600",
        "retroarch_core": "",
    },
    "atari7800": {
        "name": "Atari 7800",
        "retroarch_core": "",
    },
    "atarijaguar": {
        "name": "Atari Jaguar",
        "retroarch_core": "virtualjaguar",
    },
    "atarilynx": {
        "name": "Atari Lynx",
        "color": "FFBF00",
        "retroarch_core": "handy",
    },
    "coleco": {
        "name": "Colecovision",
        "retroarch_core": "bluemsx",
    },
    "daphne": {
        "name": "Daphne",
        "retroarch_core": "daphne",
    },
    "dreamcast": {
        "name": "Dreamcast",
        "color": "ED872D",
        "retroarch_core": "flycast",
    },
    "fds": {
        "name": "Famicom Disc System",
        "color": "B70E30",
        "retroarch_core": "nestopia",
    },
    "gb": {
        "name": "Game Boy",
        "color": "C0B8B1",
        "retroarch_core": "gambatte",
    },
    "gba": {
        "name": "Game Boy Advance",
        "color": "D5D5D5",
        "webretro_core": "mgba",
        "retroarch_core": "mgba",
    },
    "gbc": {
        "name": "Game Boy Color",
        "color": "77CCFF",
        "retroarch_core": "gambatte",
    },
    "gc": {
        "name": "GameCube",
        "color": "7461C7",
        "retroarch_core": "dolphin",
    },
    "mame-libretro": {
        "name": "Arcade",
        "color": "111111",
        "retroarch_core": "mame2010",
    },
    "mastersystem": {
        "name": "Sega Master System",
        "webretro_core": "genesis_plus_gx",
        "retroarch_core": "genesis_plus_gx",
    },
    "megadrive": {
        "name": "Genesis/Mega Drive",
        "color": "D03737",
        "webretro_core": "genesis_plus_gx",
        "retroarch_core": "genesis_plus_gx",
    },
    "model3": {
        "name": "Sega Model 3",
        "emulator": "Supermodel",
    },
    "gamegear": {
        "name": "Game Gear",
        "color": "3FA3C4",
        "retroarch_core": "genesis_plus_gx",
    },
    "msx": {
        "name": "MSX",
        "retroarch_core": "bluemsx",
    },
    "n64": {
        "name": "Nintendo 64",
        "color": "C76660",
        "webretro_core": "mupen64plus_next",
        "retroarch_core": "mupen64plus_next",
    },
    "nds": {
        "name": "Nintendo DS",
        "color": "39D0D0",
        "retroarch_core": "desmume",
    },
    "ngp": {
        "name": "Neo Geo Pocket",
        "retroarch_core": "mednafen_ngp",
    },
    "neogeo": {
        "name": "Neo Geo",
        "retroarch_core": "fbneo",
    },
    "ngpc": {
        "name": "Neo Geo Pocket Color",
        "retroarch_core": "mednafen_ngp",
    },
    "nes": {
        "name": "Nintendo",
        "color": "656565",
        "webretro_core": "nestopia",
        "retroarch_core": "nestopia",
    },
    "pcengine": {
        "name": "PC Engine/TurboGrafix 16",
        "color": "55B4CC",
        "retroarch_core": "mednafen_supergrafx",
    },
    "pcfx": {
        "name": "PC FX",
        "color": "55B4CC",
        "retroarch_core": "mednafen_pcfx",
    },
    "ps2": {
        "name": "Playstation 2",
        "color": "111CAA",
        "emulator": "PCSX2",
    },
    "ps3": {
        "name": "Playstation 3",
        "color": "224CAA",
        "emulator": "rpcs3",
    },
    "psp": {
        "name": "Playstation Portable",
        "color": "",
        "retroarch_core": "ppsspp",
    },
    "psx": {
        "name": "Playstation",
        "color": "E9DD00",
        "retroarch_core": "mednafen_psx",
    },
    "ports": {
        "name": "Ports",
    },
    "saturn": {
        "name": "Saturn",
        "color": "0047AB",
        "retroarch_core": "mednafen_saturn",
        "emulator": "yabuse",
    },
    "scummvm": {
        "name": "ScummVM",
        "color": "E8B500",
        "retroarch_core": "scummvm",
        "emulator": "scummvm",
    },
    "sega32x": {
        "name": "Sega 32X",
        "color": "",
        "retroarch_core": "genesis_plus_gx",
    },
    "segacd": {
        "name": "Sega CD",
        "color": "",
        "retroarch_core": "genesis_plus_gx",
    },
    "snes": {
        "name": "Super Nintendo",
        "color": "A060C7",
        "retroarch_core": "snes9x",
        "webretro_core": "snes9x",
    },
    "virtualboy": {
        "name": "Virtual Boy",
        "color": "99AA11",
        "retroarch_core": "mednafen_vb",
    },
    "wonderswan": {
        "name": "WonderSwan",
        "color": "AA88CC",
        "retroarch_core": "mednafen_wswan",
    },
    "wonderswancolor": {
        "name": "WonderSwan Color",
        "color": "BB33CC",
        "retroarch_core": "mednafen_wswan",
    },
    "wii": {
        "name": "Wii",
        "color": "",
        "retroarch_core": "dolphin",
    },
}
