from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from games.utils import skyscrape_console


class Command(BaseCommand):
    help = "Scrape all games found in a given gamelist XML file"

    def add_arguments(self, parser):
        parser.add_argument("system", type=str)

    def handle(self, *args, **options):
        game_system_slug = options["system"]
        if not game_system_slug:
            self.stdout.write(self.style.ERROR(f"No game system, or all specified"))
            return False

        if game_system_slug == "all":
            for slug in settings.GAME_SYSTEM_DEFAULTS.keys():
                scrape_out, load_out = skyscrape_console(slug)
                self.stdout.write(
                    self.style.SUCCESS(f"Successfully scraped roms for {slug}")
                )

        else:
            scrape_out, load_out = skyscrape_console(game_system_slug)
            self.stdout.write(
                self.style.SUCCESS("Successfully scraped roms for {slug}")
            )
