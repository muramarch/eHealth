from django.urls import path, include
from django.urls import re_path
from chat import routing

from . import consumers

websocket_urlpatterns = routing.websocket_urlpatterns

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
]

urlpatterns = [
    path('', include('chat.urls')),
]
