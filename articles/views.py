from django.shortcuts import render, get_object_or_404, get_list_or_404
# models
from .models import Article, Comment
from movies.models import Movie
# drf
from rest_framework import status
from rest_framework.response import Response
# drf serializers
from .serializers import ArticleSerializer, ArticleCreateSerializer, ArticleUpdateSerializer, CommentSerializer, CommentPostSerializer 
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
        article_list = get_list_or_404(Article, movie=movie_id)
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
        print(request.data)
        serializer = ArticleUpdateSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    else:  # Delete
        article.delete()
        return Response({"Success" : True})

@api_view(['GET', 'POST', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def article_comment(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.method == 'GET':
        comments = article.article_comments.order_by('-pk')
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        # 영화는 직접 넣어서 와야함
        request.data['user'] = request.user.id
        request.data['article'] = article_id
        serializer = CommentPostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    else:  # DELETE
        print(request.data)
        comment = get_object_or_404(Comment, pk=request.data['comment_id'])
        comment.delete()
        return Response({"Success" : True})

