from django.shortcuts import render, get_object_or_404
from .models import Genre, Movie
from .serializers import GenreSerializer, MovieSerializer
import requests
# Create your views here.
# 영화 가져와서 db에 넣는 로직
def getmovies(request):
    for page in range(1, 6):
        URL = f'https://api.themoviedb.org/3/movie/popular?api_key=4507744d222eb5c01174a9eb93bdf2af&language=ko-KR&page={page}'
        movies = requests.get(URL).json().get('results')
        for movie in movies:
            backdrop_path = movie.get('backdrop_path') if movie.get('backdrop_path') else ''
            movie_instance = Movie(
                id=movie.get('id'), adult=movie.get('adult'), 
                video=movie.get('video'), poster_path=movie.get('poster_path'),
                backdrop_path=backdrop_path, title=movie.get('title'),
                overview=movie.get('overview'), original_title=movie.get('original_title'),
                original_language=movie.get('original_language'), release_date=movie.get('release_date'),
                popularity=movie.get('popularity'), vote_count=movie.get('vote_count'),
                vote_average=movie.get('vote_average'),
                )
            movie_instance.save()
            # 장르 가져와서 연결하는 로직
            genres = movie.get('genre_ids')
            for genre in genres:
                genre_instance = get_object_or_404(Genre, pk=genre)
                movie_instance.genres.add(genre_instance)
            
            
# 장르 저장 로직
def getgenres(request):
    URL = 'https://api.themoviedb.org/3/genre/movie/list?api_key=4507744d222eb5c01174a9eb93bdf2af'
    response = requests.get(URL)
    for genre in response.json().get('genres'):
        genre = Genre(id=genre.get('id'), name=genre.get('name'))
        genre.save()