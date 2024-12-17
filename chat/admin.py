from django.contrib import admin
from .models import MessageModel, RoomModel

# Register your models here.
admin.site.register(RoomModel)
admin.site.register(MessageModel)