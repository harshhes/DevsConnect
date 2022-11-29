from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('',home),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]