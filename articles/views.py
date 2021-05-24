from django.shortcuts import render, get_object_or_404, get_list_or_404
# models
from .models import Article, Comment
from movies.models import Movie
# drf
from rest_framework import status
from rest_framework.response import Response
# drf serializers
from .serializers import ArticleSerializer, ArticleCreateSerializer, CommentSerializer
# jwt
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

# 모든 리뷰 GET
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def articles(request):
    article_list = Article.objects.select_related('movie').select_related('user').order_by('-pk')
    serializer = ArticleSerializer(article_list, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# GET POST로 GET은 목록, POST는 글 작성으로 변경해야 할까?
@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def movie_article(request, movie_id):
    if request.method =="GET":
        article_list = get_list_or_404(Article)
        serializer = ArticleSerializer(article_list, many=True)
        return Response(serializer.data)
    else:  # POST
        request.data['user'] = request.user.id
        serializer = ArticleCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

# 여기서의 GET PUT DELETE는 글 한개에 대한 GET PUT DELETE
@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.method =="GET":
        serializer = ArticleSerializer(article)
        return Response({'article' : serializer.data, 'isAuthor' : request.user==article.user})
    elif request.method =="PUT":
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    else:  # Delete
        article.delete()
        return Response({"Success" : True})
