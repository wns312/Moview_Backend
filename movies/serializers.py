from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Movie, Genre
class MovieSerializer(serializers.ModelSerializer):
  pass


class GenreSerializer(serializers.ModelSerializer):
  class Meta:
    Model = Genre
    fields = '__all__'