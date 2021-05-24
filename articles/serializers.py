from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Article, Comment
from movies.serializers import MovieSerializer
from accounts.serializers import UserSerializer

class ArticleSerializer(serializers.ModelSerializer):
  user = UserSerializer(read_only=True)
  movie = MovieSerializer(read_only=True)
  class Meta:
    model = Article
    # like users는 생성단계에서 들어가지 않는다.
    fields = '__all__'


class ArticleCreateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Article
    # like users는 생성단계에서 들어가지 않는다.
    fields = ('title', 'content', 'movie', 'user')


class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = '__all__'