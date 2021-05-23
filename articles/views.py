from django.shortcuts import render, get_object_or_404, get_list_or_404
# models
from .models import Article, Comment
# drf
from rest_framework import status
from rest_framework.response import Response
# drf serializers
from .serializers import ArticleSerializer, CommentSerializer
# jwt
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
# Create your views here.
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def article(request, article_id, movie_id):
    pass
