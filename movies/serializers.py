from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Movie, Genre, Prefer
from accounts.serializers import UserSerializer

# Indentation 2로 설정되어 있음 주의!



class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'



class MovieSerializer(serializers.ModelSerializer):
    # prefer_users = UserSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'

# Detail에서 Prefer와 영화 정보를 같이 가져오기 위한 용도
class PreferSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)
    class Meta:
        model = Prefer
        fields = '__all__'

# Prefer 새로운 평점 저장을 위한 용도
class PreferSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prefer
        fields = '__all__'