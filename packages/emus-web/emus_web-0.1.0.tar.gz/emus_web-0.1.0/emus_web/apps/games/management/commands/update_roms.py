from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from games.tasks import update_roms


class Command(BaseCommand):
    help = "Scrape + import all games for all systems"

    def add_arguments(self, parser):
        parser.add_argument(
            "--full-scan",
            action="store_true",
            help="Update all files, even ones we already know about",
        )

    def handle(self, *args, **options):
        all_slugs = settings.GAME_SYSTEM_DEFAULTS.keys()
        update_roms(all_slugs, full_scan=options["full_scan"])
        self.stdout.write(
            self.style.SUCCESS("Successfully scraped and imported roms")
        )
