from rest_framework import generics, status, permissions
from django.contrib.auth.models import User
from rest_framework.response import Response
from .serializers import CreateSerializer

class UserViews(generics.RetrieveAPIView):
  permission_classes = [permissions.IsAuthenticated]
  serializer_class = CreateSerializer

  def get_object(self):
    return self.request.user
  
class CreateViews(generics.CreateAPIView):
  serializer_class = CreateSerializer

  def post(self, request):
    serializer = self.get_serializer(data=request.data)
    if serializer.is_valid():
      user = serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
