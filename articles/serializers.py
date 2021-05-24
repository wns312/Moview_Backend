from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Article, Comment

class ArticleSerializer(serializers.ModelSerializer):
  class Meta:
    model = Article
    # like users는 생성단계에서 들어가지 않는다.
    fields = ('title', 'content', 'movie', 'user')


class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = '__all__'