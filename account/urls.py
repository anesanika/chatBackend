from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import CreateViews, UserViews

urlpatterns = [
  path('access/', TokenObtainPairView.as_view()),
  path('create/', CreateViews.as_view()),
  path('me/', UserViews.as_view())
]