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

    # 중개 모델 필드 정의
    # 이 필드를 통해 영화 id를 가져와서 장르를 취합 한 뒤, 보내주고 이후 state에서 관리
    # 영화 선호 추가시 state와 id추가를 각자 해줘서 DB 접근 최소화
    # 영화 선호 목록 추가 기준은 더 고민해볼것
    prefer_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='prefer_movies', through='Prefer')


# 모델과 유저의 manytomany 중개모델을 직접 만들어야 한다..
# 바로 여기
class Prefer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField()  # choice로 바꾸고 싶은데 나중에 생각하자.. 0~10

class Genre(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    # Many to Many
    movies = models.ManyToManyField(Movie, related_name='genres')

