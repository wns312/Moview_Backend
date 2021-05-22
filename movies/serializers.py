from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Movie, Genre, Prefer

# Indentation 2로 설정되어 있음 주의!

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
      model = Movie
      fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
      model = Genre
      fields = '__all__'

class PreferSerializer(serializers.ModelSerializer):

    class Meta:
        model = Prefer
        fields = '__all__'