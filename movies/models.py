from django.db import models
from django.contrib.auth import settings

# Create your models here.
class Movie(models.Model):
    id = models.BigAutoField(primary_key=True)
    
    adult = models.BooleanField()
    video = models.BooleanField()

    poster_path = models.CharField(max_length=100)
    backdrop_path = models.CharField(max_length=100)

    title = models.CharField(max_length=200)
    overview = models.TextField()

    original_title = models.CharField(max_length=200)
    original_language = models.CharField(max_length=50)
    
    release_date = models.DateField()
    popularity = models.FloatField()

    vote_average = models.FloatField()
    vote_count = models.IntegerField()

class Genre(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    # Many to Many
    movies = models.ManyToManyField(Movie, related_name='genres')


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 참조 필드 : 모델 연결 어떻게 하는지 기억해내기
    # 어떤 영화가 주제 <-> 특정 영화를 주제로 작성된 글 모아오기
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_articles')
    # 작성자 <-> 특정 유저가 작성한 글 모아오기
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_articles')
    # 이 글에 좋아요 누른 유저 목록 <-> 유저가 좋아요 누른 글목록
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')


class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 참조 필드
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_comments')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='article_comments')