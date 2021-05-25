from rest_framework import serializers
from django.contrib.auth import get_user_model
class UserSerializer(serializers.ModelSerializer):
  password = serializers.CharField(write_only=True)
  class Meta:
    model = get_user_model()
    fields = ('username', 'email', 'is_recommended', 'password')

class UserUpdateSerializer(serializers.ModelSerializer):
  class Meta:
    model = get_user_model()
    fields = ('is_recommended',)