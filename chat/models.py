from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class RoomModel(models.Model):
  name = models.CharField(max_length=255)
  slug = models.SlugField(unique=True)

class MessageModel(models.Model):
  message = models.TextField()
  room = models.ForeignKey(RoomModel, related_name=("message"), on_delete=models.CASCADE)
  user = models.ForeignKey(User, related_name=("message"), on_delete=models.CASCADE)