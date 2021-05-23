from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Article, Comment

class ArticleSerializer(serializers.ModelSerializer):
  class Meta:
    model = Article
    fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = '__all__'