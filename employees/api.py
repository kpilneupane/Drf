from rest_framework import generics
from .serializers import MessageSerializer
from .models import Messages


class MessageApi(generics.ListCreateAPIView):
    queryset = Messages.objects.all()
    serializer_class = MessageSerializer
