from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("rick_and_morty.urls", namespace="rick_and_morty"))
]
