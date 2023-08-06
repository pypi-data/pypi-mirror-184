from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from games.utils import export_collections


class Command(BaseCommand):
    help = "Export all collections to media directory"

    def handle(self, *args, **options):
        export_collections(dryrun=False)
        return


