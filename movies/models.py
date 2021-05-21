from django.db import models

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


# 모델과 유저의 manytomany 중개모델을 직접 만들어야 한다..
# 바로 여기