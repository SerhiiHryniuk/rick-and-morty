from django.urls import path

from rick_and_morty.views import get_random_character_view

app_name = "rick_and_morty"

urlpatterns = [
    path(
        "characters/random/",
        get_random_character_view,
        name="random_character"
    )
]
