from rest_framework import generics
from .serializer import PlayersSerializer
from .models import Players


class PlayersApi(generics.ListCreateAPIView):
    queryset = Players.objects.all()
    serializer_class = PlayersSerializer
