from django.urls import path, include
from rest_framework import routers
from .views import RoomVeiw, MessageListView

router = routers.DefaultRouter()
router.register(r'room', RoomVeiw, basename="room-model")

urlpatterns = [
  path('', include(router.urls)),
  path('rooms/<slug:slug>/messages/', MessageListView.as_view(), name='message-list')
]
