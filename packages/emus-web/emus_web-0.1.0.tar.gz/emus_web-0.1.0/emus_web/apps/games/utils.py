from games.constants import (
    ENGLISH_PATCHED_KEYWORDS,
    HACK_KEYWORDS,
    REGION_KEYWORDS,
    UNDUB_KEYWORDS,
)
import os
import xml.etree.ElementTree as ET
import subprocess
import re

from dateutil import parser
from django.conf import settings

from .models import (
    Developer,
    Game,
    GameSystem,
    Genre,
    Publisher,
    GameCollection,
)

import logging

logger = logging.Logger(__name__)


def update_media_root_for_import(file_path):
    """Given a file path, re-write it for our app MEDIA_ROOT"""
    suffix = ""
    if file_path:
        suffix = file_path.split("/media/")[-1]
    return suffix


def import_gamelist_file_to_db_for_system(
    game_system_slug, file_path=None, full_scan=False
):
    imported_games = []
    not_imported_games = []
    if not file_path:
        file_path = os.path.join(
            settings.ROMS_DIR, game_system_slug, "gamelist.xml"
        )
    if not os.path.exists(file_path):
        logger.info(
            "File path for {game_system_slug} had no gamelist.xml file, run a scraper first!"
        )
        return

    gamelist = ET.parse(file_path)
    game_system = GameSystem.objects.filter(
        retropie_slug=game_system_slug
    ).first()
    if not game_system:
        defaults = settings.GAME_SYSTEM_DEFAULTS.get(game_system_slug, None)
        full_system_name = game_system_slug
        if defaults:
            full_system_name = defaults.get("name", game_system_slug)
        game_system = GameSystem.objects.create(
            name=full_system_name, retropie_slug=game_system_slug
        )

    games = gamelist.findall("game")
    for game in games:
        name = game.find("name").text
        game_path = game.find("path").text.lower()
        try:
            obj, created = Game.objects.get_or_create(
                name=name, game_system=game_system
            )
        except Game.MultipleObjectsReturned:
            logger.warning(
                f"While importing {name} for {game_system}, duplicate entry found"
            )
            print(
                f"While importing {name} for {game_system}, duplicate entry found"
            )
            continue

        if not created and not full_scan:
            not_imported_games.append(obj)
            logger.info(f"Not updating {obj}, use full-scan to update")
            print(f"Not updating {obj}, use full-scan to update")
            continue
        elif not created and full_scan:
            print(f"Updating {obj}")
        else:
            print(f"Adding {obj}")

        region = Game.Region.X.name

        if any(us in game_path for us in REGION_KEYWORDS["US"]):
            region = Game.Region.US.name
        if any(jp in game_path for jp in REGION_KEYWORDS["JP"]):
            region = Game.Region.JP.name
        if any(eu in game_path for eu in REGION_KEYWORDS["EU"]):
            region = Game.Region.EU.name

        english_patched = any(
            key in game_path.lower() for key in ENGLISH_PATCHED_KEYWORDS
        )
        patch_version = None
        if english_patched:
            version_re = re.search("(?= v)(.*?)(?=\))", game_path.lower())
            if version_re:
                patch_version = version_re.group(0)[2:]
        undub = any(key in game_path.lower() for key in UNDUB_KEYWORDS)
        hack = any(key in game_path.lower() for key in HACK_KEYWORDS)

        release_date_str = game.find("releasedate").text
        developer_str = game.find("developer").text
        publisher_str = game.find("publisher").text
        genres_str = game.find("genre").text

        rating_str = game.find("rating").text
        players_str = "1"
        if game.find("players"):
            players_str = game.find("players").text
        try:
            kid_game = game.find("kidgame").text == "true"
        except AttributeError:
            kid_game = False

        genre_list = []
        if genres_str:
            genre_str_list = genres_str.split(", ")
            for genre_str in genre_str_list:
                genre, _created = Genre.objects.get_or_create(name=genre_str)
                genre_list.append(genre)

        players = int(players_str) if players_str else 1
        rating = float(rating_str) if rating_str else None
        publisher = None
        if publisher_str:
            publisher, _created = Publisher.objects.get_or_create(
                name=publisher_str
            )
        developer = None
        if developer_str:
            developer, _created = Developer.objects.get_or_create(
                name=developer_str
            )
        release_date = (
            parser.parse(release_date_str) if release_date_str else None
        )
        description = game.find("desc").text
        screenshot_path = update_media_root_for_import(game.find("image").text)
        rom_path = update_media_root_for_import(game.find("path").text)
        video_path_elem = game.find("video")
        video_path = ""
        if video_path_elem:
            video_path = update_media_root_for_import(video_path_elem.text)
        marquee_path = update_media_root_for_import(game.find("marquee").text)

        obj.game_system = game_system
        obj.developer = developer
        obj.publisher = publisher
        obj.players = players
        obj.description = description
        obj.release_date = release_date
        obj.rating = rating
        obj.genre.set(genre_list)
        obj.screenshot = screenshot_path
        obj.rom_file = rom_path
        obj.video = video_path
        obj.marquee = marquee_path
        obj.kid_game = kid_game
        obj.english_patched = english_patched
        obj.english_patched_version = patch_version
        obj.hack = hack
        obj.undub = undub
        obj.region = region
        obj.save()

        imported_games.append(obj)
    return {"imported": imported_games, "not_imported": not_imported_games}


def export_gamelist_file_to_path_for_system(game_system_slug, file_path=None):
    exported_games = []
    game_system = GameSystem.objects.get(retropie_slug=game_system_slug)

    if not file_path:
        file_path = f"/tmp/{game_system_slug}-gamelist.xml"
        # file_path = os.path.join(settings.ROMS_DIR, game_system_slug, "gamelist.xml")

    root = ET.Element("gameList")

    tree = ET.ElementTree(root)
    tree.write(file_path)
    games = Game.objects.filter(game_system=game_system)
    for game in games:
        game_node = ET.SubElement(root, "game")

        genre_str = ", ".join(game.genre.all().values_list("name", flat=True))
        release_date_str = ""
        if game.release_date:
            release_date_str = game.release_date.strftime("%Y%m%dT00000")
        ET.SubElement(game_node, "path").text = (
            game.rom_file.path if game.rom_file else ""
        )
        ET.SubElement(game_node, "name").text = game.name
        ET.SubElement(game_node, "thumbnail").text = ""
        ET.SubElement(game_node, "image").text = (
            game.screenshot.path if game.screenshot else ""
        )
        ET.SubElement(game_node, "marquee").text = (
            game.marquee.path if game.marquee else ""
        )
        ET.SubElement(game_node, "video").text = (
            game.video.path if game.video else ""
        )
        ET.SubElement(game_node, "rating").text = str(game.rating)
        ET.SubElement(game_node, "desc").text = game.description
        ET.SubElement(game_node, "releasedate").text = release_date_str
        ET.SubElement(game_node, "developer").text = str(game.developer)
        ET.SubElement(game_node, "publisher").text = str(game.publisher)
        ET.SubElement(game_node, "genre").text = genre_str
        ET.SubElement(game_node, "players").text = str(game.players)
        if game.kid_game:
            ET.SubElement(game_node, "kidgame").text = "true"

        exported_games.append(game)
    tree = ET.ElementTree(root)
    tree.write(file_path, xml_declaration=True, encoding="utf-8")

    return exported_games, file_path


def skyscrape_console(game_system_slug):
    scraper_config = settings.SCRAPER_CONFIG_FILE
    scraper_binary = settings.SCRAPER_BIN_PATH
    scraper_site = settings.SCRAPER_SITE
    scraper_frontend = settings.SCRAPER_FRONTEND

    # If the config file is relative, append our base dir
    if scraper_config[0] != "/":
        scraper_config = os.path.join(settings.BASE_DIR, scraper_config)
    if not os.path.exists(scraper_config):
        logger.info(f"Config file not found at {scraper_config}")
        return
    logger.info(
        f"Scraping game info using configuration file from {scraper_config}"
    )

    scrape_output = subprocess.run(
        [
            scraper_binary,
            "-c",
            f"{scraper_config}",
            "-s",
            f"{scraper_site}",
            "-f",
            f"{scraper_frontend}",
            "-p",
            f"{game_system_slug}",
        ],
        capture_output=True,
    )
    load_output = subprocess.run(
        [
            scraper_binary,
            "-c",
            f"{scraper_config}",
            "-f",
            f"{scraper_frontend}",
            "-p",
            f"{game_system_slug}",
        ],
        capture_output=True,
    )
    # TODO We should progressively pipe output to a log file instead of this
    # print(scrape_output)
    # print(load_output)
    print(f"Scraped info for {game_system_slug}")
    return scrape_output, load_output


def export_collections(dryrun=True):
    exported = []
    for collection in GameCollection.objects.all():
        collection.export_to_file(dryrun)
        exported.append(collection)
    return exported
