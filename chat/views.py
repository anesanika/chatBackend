from django.shortcuts import render
from rest_framework import permissions, viewsets, generics
from .models import RoomModel, MessageModel
from .serializer import RoomSerializer, MessageSerializer 

# Create your views here.

class RoomVeiw(viewsets.ModelViewSet):
  permission_classes = [permissions.IsAuthenticated, ]
  queryset = RoomModel.objects.all()

  serializer_class = RoomSerializer
  

class MessageListView(generics.ListAPIView):

    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def get_queryset(self):
        room_slug = self.kwargs['slug']
        room = RoomModel.objects.get(slug=room_slug) 
        return MessageModel.objects.filter(room=room)