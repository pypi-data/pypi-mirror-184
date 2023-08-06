from django.conf import settings
from django.core.management.base import BaseCommand

from games.utils import import_gamelist_file_to_db_for_system


class Command(BaseCommand):
    help = "Import all games found in a given gamelist XML file"

    def add_arguments(self, parser):
        parser.add_argument("system", type=str)
        parser.add_argument(
            "--file",
            action="store_true",
            help="Import from specific file",
        )
        parser.add_argument(
            "--full-scan",
            action="store_true",
            help="Update all files, even ones we already know about",
        )

    def import_from_slug(self, slug, file_path, full_scan=False):
        results = import_gamelist_file_to_db_for_system(slug, file_path, full_scan)

        if not results:
            self.style.ERROR(
                "No games imported for {slug}, check for gamelist.xml file or re-run scraper"
            )
            return

        imported = results["imported"]
        not_imported = results["not_imported"]

        if imported:
            self.stdout.write(
                self.style.SUCCESS(
                    f"Successfully imported {len(imported)} games for {slug}"
                )
            )
        if not_imported:
            self.stdout.write(
                self.style.SUCCESS(
                    f"Found, but did not update {len(not_imported)} games for {slug} (use --full-scan to update)"
                )
            )
        if not imported and not not_imported:
            self.stdout.write(
                self.style.ERROR(
                    "No games imported for {slug}, check for gamelist.xml file or re-run scraper"
                )
            )

    def handle(self, *args, **options):
        game_system_slug = options["system"]
        if not game_system_slug:
            self.style.ERROR(
                "Please provide a game system slug, or all to import from all systems"
            )
            return False
        if game_system_slug == "all":
            for slug in settings.GAME_SYSTEM_DEFAULTS.keys():
                self.import_from_slug(slug, options["file"], options["full_scan"])
        else:
            self.import_from_slug(
                game_system_slug, options["file"], options["full_scan"]
            )
