from django.urls import path
from .api import PlayersApi


urlpatterns = [
    path('api', PlayersApi.as_view())
]