import os
from typing import Optional

password = os.getenv('SCREENSCRAPER_DEV_PASSWORD', 'a88e9PGPlldlmaLRlkNH8naEl')
user = os.getenv('SCREENSCRAPER_USERNAME', 'secstate')
base_scraper_url = f"https://www.screenscraper.fr/api2/jeuInfos.php?softname=emus&ssid={user}&sspassword={password}&output=json&{0}"

def query_screenscraper_fr(search_name: str, platform_id: Optional[int]):
    scraper_url = base_scraper_url.format(search_name)
    print(scraper_url)

# + (platformId.isEmpty()?"":"&systemeid=" + platformId) + "&output=json&" + searchName;
