import random

from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from rick_and_morty.models import Character
from rick_and_morty.serializers import CharacterSerializer


@api_view(["GET"])
def get_random_character_view(request: Request) -> Response:
    primary_keys = Character.objects.values_list("pk", flat=True)
    random_primary_key = random.choice(primary_keys)
    random_character = Character.objects.get(pk=random_primary_key)
    serializer = CharacterSerializer(random_character)
    return Response(serializer.data, status=status.HTTP_200_OK)


class CharacterListView(generics.ListAPIView):
    serializer_class = CharacterSerializer

    def get_queryset(self):
        queryset = Character.objects.all()
        name = self.request.query_params.get("name")
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset
