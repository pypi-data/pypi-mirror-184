from celery import shared_task

# from celery.log import get_task_logger

from games.utils import import_gamelist_file_to_db_for_system, skyscrape_console

# logging = get_task_logger()


@shared_task
def update_roms(game_system_slugs: list, full_scan=False):
    import_dict = {"imported": [], "not_imported": []}
    for game_system_slug in game_system_slugs:
        skyscrape_console(game_system_slug)
        import_dict = import_gamelist_file_to_db_for_system(
            game_system_slug, full_scan=full_scan
        )
    if import_dict["imported"]:
        import_dict["imported"] = [game.name for game in import_dict["imported"]]
    if import_dict["not_imported"]:
        import_dict["not_imported"] = [
            game.name for game in import_dict["not_imported"]
        ]
    # logging.info(import_dict)
