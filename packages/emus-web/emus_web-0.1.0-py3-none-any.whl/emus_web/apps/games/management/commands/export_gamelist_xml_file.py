import xml.etree.ElementTree as ET

from django.core.management.base import BaseCommand, CommandError

from games.utils import export_gamelist_file_to_path_for_system


class Command(BaseCommand):
    help = "Export all games found to a given gamelist XML file"

    def add_arguments(self, parser):
        parser.add_argument("system", type=str)
        parser.add_argument(
            "--file",
            action="store_true",
            help="Export to a specific file",
        )

    def handle(self, *args, **options):
        games, file_path = export_gamelist_file_to_path_for_system(
            options["system"],
            options["file"],
        )
        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully exported {len(games)} games to {file_path}"
            )
        )
