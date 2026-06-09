from rest_framework import serializers

from rick_and_morty.models import Character


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = [
            "id",
            "api_id",
            "name",
            "status",
            "species",
            "gender",
            "image"
        ]
