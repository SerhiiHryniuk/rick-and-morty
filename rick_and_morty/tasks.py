from celery import shared_task

from rick_and_morty.scrapper import sync_characters_with_api


@shared_task
def run_sync_with_api() -> None:
    sync_characters_with_api()
