import logging
import os
import uuid
from shlex import quote

from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django_extensions.db.models import TimeStampedModel
from emus_web.utils import ChoiceEnum
from taggit.managers import TaggableManager

logger = logging.getLogger(__name__)


def get_screenshot_upload_path(instance, filename):
    return f"{instance.game_system.retropie_slug}/screenshots/{filename}"


def get_marquee_upload_path(instance, filename):
    return f"{instance.game_system.retropie_slug}/marquee/{filename}"


def get_video_upload_path(instance, filename):
    return f"{instance.game_system.retropie_slug}/videos/{filename}"


def get_rom_upload_path(instance, filename):
    return f"{instance.game_system.retropie_slug}/{filename}"


class BaseModel(TimeStampedModel):
    """A base model for providing name and slugged fields for organizational models"""

    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from="name")

    class Meta:
        ordering = ["name"]
        abstract = True

    def slugify_function(self, content):
        for element in settings.REMOVE_FROM_SLUGS:
            content = content.replace(element, "-")
        return content.lower()

    def __str__(self):
        return self.name


class StatisticsMixin(models.Model):
    class Meta:
        abstract = True

    @property
    def rating_avg(self):
        avg = self.game_set.aggregate(models.Avg("rating"))["rating__avg"]
        if avg:
            return int(100 * avg)
        return 0


class Genre(BaseModel, StatisticsMixin):
    def get_absolute_url(self):
        return reverse("games:genre_detail", args=[self.slug])


class Publisher(BaseModel, StatisticsMixin):
    def get_absolute_url(self):
        return reverse("games:publisher_detail", args=[self.slug])


class Developer(BaseModel, StatisticsMixin):
    def get_absolute_url(self):
        return reverse("games:developer_detail", args=[self.slug])


class GameSystem(BaseModel, StatisticsMixin):
    retropie_slug = models.CharField(
        blank=True,
        null=True,
        max_length=50,
    )
    color = models.CharField(
        blank=True,
        null=True,
        max_length=6,
        help_text="Hex value for console badges",
    )

    @property
    def defaults(self):
        return settings.GAME_SYSTEM_DEFAULTS.get(self.retropie_slug, None)

    @property
    def get_color(self):
        color = self.color
        if not color and self.defaults:
            color = self.defaults.get("color", "")
        return color

    @property
    def webretro_core(self):
        core = None
        if self.defaults:
            core = self.defaults.get("webretro_core", None)
        return core

    def get_absolute_url(self):
        return reverse("games:game_system_detail", args=[self.slug])


class Game(BaseModel):
    class Region(ChoiceEnum):
        US = "USA"
        EU = "Europe"
        JP = "Japan"
        X = "Unknown"

    game_system = models.ForeignKey(
        GameSystem,
        on_delete=models.SET_NULL,
        null=True,
    )
    release_date = models.DateField(
        blank=True,
        null=True,
    )
    developer = models.ForeignKey(
        Developer,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    genre = models.ManyToManyField(
        Genre,
    )
    players = models.SmallIntegerField(
        default=1,
    )
    kid_game = models.BooleanField(
        default=False,
    )
    description = models.TextField(
        blank=True,
        null=True,
    )
    rating = models.FloatField(
        blank=True,
        null=True,
        validators=[MaxValueValidator(1), MinValueValidator(0)],
    )
    video = models.FileField(
        blank=True,
        null=True,
        max_length=300,
        upload_to=get_video_upload_path,
    )
    marquee = models.ImageField(
        blank=True,
        null=True,
        max_length=300,
        upload_to=get_marquee_upload_path,
    )
    screenshot = models.ImageField(
        blank=True,
        null=True,
        max_length=300,
        upload_to=get_screenshot_upload_path,
    )
    rom_file = models.FileField(
        blank=True,
        null=True,
        max_length=300,
        upload_to=get_rom_upload_path,
    )
    hack = models.BooleanField(
        default=False,
    )
    hack_version = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    english_patched = models.BooleanField(
        default=False,
    )
    english_patched_version = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )
    undub = models.BooleanField(
        default=False,
    )
    region = models.CharField(
        max_length=10,
        choices=Region.choices(),
        blank=True,
        null=True,
    )
    source = models.CharField(
        max_length=500,
        blank=True,
        null=True,
    )
    featured_on = models.DateField(
        blank=True,
        null=True,
    )

    tags = TaggableManager(blank=True)

    class Meta:
        ordering = ["game_system", "name"]

    def __str__(self):
        return f"{self.name} for {self.game_system}"

    def get_absolute_url(self):
        return reverse("games:game_detail", args=[self.slug])

    @property
    def rating_by_100(self) -> float:
        if self.rating:
            return int(100 * self.rating)
        return int(0)

    @property
    def rating_class(self):
        if self.rating_by_100 > 70:
            return "high"
        if self.rating_by_100 > 50:
            return "medium"
        return "low"

    @property
    def in_progress(self):
        return self.started_on and not self.finished_on

    @property
    def retroarch_core_path(self):
        path = None
        retroarch_core = self.game_system.defaults.get("retroarch_core", None)
        if retroarch_core:
            path = quote(
                os.path.join(
                    settings.ROMS_DIR,
                    "cores",
                    retroarch_core + "_libretro.so",
                )
            )
        return path

    @property
    def webretro_url(self):
        if "webretro_core" in self.game_system.defaults.keys():
            return reverse("games:game_play_detail", args=[self.slug])

    def retroarch_cmd(self, platform="linux"):
        if platform != "linux":
            return ""
        if not self.retroarch_core_path:
            return ""
        if not self.rom_file:
            return ""
        rom_file = quote(self.rom_file.path)
        if self.game_system.slug == "scummvm":
            new_path = list()
            try:
                split_path = self.rom_file.path.split("/")
                folder_name = self.rom_file.path.split("/")[-1].split(".")[0]
                for i in split_path:
                    if i == "scummvm":
                        new_path.append(f"scummvm/{folder_name}")
                    else:
                        new_path.append(i)
            except IndexError:
                pass
            if new_path:
                rom_file = quote("/".join(new_path))
        if not os.path.exists(self.retroarch_core_path):
            logger.info(
                f"Missing libretro core file at {self.retroarch_core_path}"
            )
            return f"Libretro core not found at {self.retroarch_core_path}"

        return f"retroarch -L {self.retroarch_core_path} {rom_file} -v"

    def cmd(self, platform="linux"):
        cmd = None
        if self.retroarch_cmd(platform):
            return self.retroarch_cmd(platform)

        rom_file = quote(self.rom_file.path)
        emulator = self.game_system.defaults.get("emulator", None)
        if emulator == "PCSX2":
            cmd = f"{emulator} --console --fullscreen --nogui {rom_file}"
        return cmd


class GameCollection(BaseModel):
    games = models.ManyToManyField(Game)
    game_system = models.ForeignKey(
        GameSystem,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    developer = models.ForeignKey(
        Developer,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse("games:gamecollection_detail", args=[self.slug])

    @property
    def rating_avg(self):
        avg = self.games.aggregate(models.Avg("rating"))["rating__avg"]
        if avg:
            return int(100 * avg)
        return 0

    def export_to_file(self, dryrun=True):
        """Will dump this collection to a .cfg file in /tmp or
        our COLLECTIONS_DIR configured path if dryrun=False"""

        collection_slug = self.slug.replace("-", "")
        file_path = f"/tmp/custom-{collection_slug}.cfg"
        if not dryrun:
            file_path = os.path.join(
                settings.COLLECTIONS_DIR, f"custom-{collection_slug}.cfg"
            )

        with open(file_path, "w") as outfile:
            for game in self.games.all():
                outfile.write(game.rom_file.path + "\n")
