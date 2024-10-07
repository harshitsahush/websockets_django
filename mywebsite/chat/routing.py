#in order to use this consimer we need to use some routing

from django.urls import re_path
from . import consumers


websocket_urlpatterns = [
    re_path(r'ws/socket-server/', consumers.ChatConsumer.as_asgi())
]