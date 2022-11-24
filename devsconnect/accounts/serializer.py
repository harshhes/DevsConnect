from rest_framework import serializers
from django.contrib.auth.models import User

class Register(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email','first_name', 'last_name', 'password']