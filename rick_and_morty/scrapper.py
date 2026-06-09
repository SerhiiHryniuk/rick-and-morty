import time
import requests
from django.conf import settings

from rick_and_morty.models import Character


def scrape_characters() -> list[Character]:
    url_to_scrape = settings.RICK_AND_MORTY_CHARACTERS_API_URL

    characters = []
    while url_to_scrape is not None:
        response = requests.get(url_to_scrape)

        if response.status_code == 429:
            time.sleep(1)
            continue

        response.raise_for_status()
        characters_response = response.json()

        for character in characters_response["results"]:
            characters.append(
                Character(
                    api_id=character["id"],
                    name=character["name"],
                    status=character["status"],
                    species=character["species"],
                    gender=character["gender"],
                    image=character["image"],
                )
            )

        url_to_scrape = characters_response["info"]["next"]

    return characters


def save_characters(characters: list[Character]) -> None:
    for character in characters:
        character.save()


def sync_characters_with_api() -> None:
    characters = scrape_characters()
    save_characters(characters)
