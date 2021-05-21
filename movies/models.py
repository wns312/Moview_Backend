from django.db import models

# Create your models here.
class Movie(models.Model):
    id = models.BigAutoField(primary_key=True)
    
    adult = models.BooleanField(blank=True)
    video = models.BooleanField(blank=True)

    poster_path = models.CharField(max_length=100, blank=True)
    backdrop_path = models.CharField(max_length=100, blank=True)

    title = models.CharField(max_length=200, blank=True)
    overview = models.TextField(blank=True)

    original_title = models.CharField(max_length=200, blank=True)
    original_language = models.CharField(max_length=50, blank=True)
    
    release_date = models.DateField(blank=True)
    popularity = models.FloatField(blank=True)

    vote_average = models.FloatField(blank=True)
    vote_count = models.IntegerField(blank=True)

class Genre(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    # Many to Many
    movies = models.ManyToManyField(Movie, related_name='genres')