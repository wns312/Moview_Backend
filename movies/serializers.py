from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Movie, Genre
class MovieSerializer(serializers.ModelSerializer):
  class Meta:
    Model = Movie
    fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
  class Meta:
    Model = Genre
    fields = '__all__'