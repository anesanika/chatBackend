from rest_framework import serializers
from .models import RoomModel, MessageModel

class RoomSerializer(serializers.ModelSerializer):
  class Meta:
    model = RoomModel
    fields = "__all__"

class MessageSerializer(serializers.ModelSerializer):
  username = serializers.CharField(source="user.username", read_only=True)
  class Meta:
    model = MessageModel
    fields = ['id', 'message', 'room', 'user', 'username']