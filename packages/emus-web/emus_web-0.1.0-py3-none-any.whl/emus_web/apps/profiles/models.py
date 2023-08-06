from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models.deletion import CASCADE, DO_NOTHING
from django.utils import timezone
from django_extensions.db.models import TimeStampedModel
from simple_history.models import HistoricalRecords
from django.db.models import F, Q

from games.models import Game

User = get_user_model()


class UserGamePlaythrough(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=DO_NOTHING)
    started_ts = models.DateTimeField(default=timezone.now, blank=True)
    finished_ts = models.DateTimeField(blank=True, null=True)
    percent = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(100), MinValueValidator(0)],
        help_text="Keeps track of how far through the game you are",
    )
    history = HistoricalRecords()

    def __str__(self):
        return f"Progress in {self.game} for {self.user} ({self.percent}%)"

    def create_update(self):
        """Add an update to our playthrough"""
        if self.progress:
            return self.usergameplaythroughupdate_set.create(
                user=self.user, percent=self.percent
            )
        return None

    class Meta:
        """Don't let playthroughs end before they start"""

        constraints = [
            models.CheckConstraint(
                check=Q(finished_ts__gte=F("started_ts")), name="chronology"
            )
        ]
        ordering = ("-started_ts",)


class UserGamePlaythroughUpdate(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    playthrough = models.ForeignKey(
        UserGamePlaythrough, on_delete=models.DO_NOTHING
    )
    percent = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(100), MinValueValidator(0)],
        help_text="Keeps track of how far through the game you are",
    )

    def __str__(self):
        return f"Progress in {self.game} for {self.user} ({self.percent}%)"

    def save(self, *args, **kwargs):
        """Can't hide from us, user was active!"""
        self.user.user_profile.update_active_date()
        super().save(*args, **kwargs)


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=CASCADE, related_name="profile"
    )
    favorite_games = models.ManyToManyField(
        Game, related_name="favorite_games"
    )
    last_active = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"User profile for {self.user}"

    def update_active_date(self):
        self.last_active = timezone.now()
        self.save()
