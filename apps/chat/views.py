from rest_framework import viewsets
from .models import Message
from .serializers import MessageSerializer

class MessageListCreateView(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer