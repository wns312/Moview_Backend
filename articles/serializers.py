from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Article, Comment

class ArticleSerializer(serializers.ModelSerializer):
  class Meta:
    Model = Article
    fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    Model = Comment
    fields = '__all__'