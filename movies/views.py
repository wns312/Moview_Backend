from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Movie, Genre, Prefer
from accounts.models import User
from .serializers import GenreSerializer, MovieSerializer, MovieListSerializer, PreferSerializer
from accounts.serializers import UserSerializer

# jwt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
# Create your views here.

# 영화 가져와서 db에 넣는 로직
@api_view(['GET'])
def getmovies(request):
    for page in range(1, 21):
        URL = f'https://api.themoviedb.org/3/movie/popular?api_key=4507744d222eb5c01174a9eb93bdf2af&language=ko-KR&page={page}'
        movies = requests.get(URL).json().get('results')
        for movie in movies:
            backdrop_path = movie.get('backdrop_path') if movie.get('backdrop_path') else ''        
            release_date = movie.get('release_date') if movie.get('release_date') else date(1000, 1, 1)
            movie_instance = Movie(
                id=movie.get('id'), adult=movie.get('adult'), 
                video=movie.get('video'), poster_path=movie.get('poster_path'),
                backdrop_path=backdrop_path, title=movie.get('title'),
                overview=movie.get('overview'), original_title=movie.get('original_title'),
                original_language=movie.get('original_language'), release_date=release_date,
                popularity=movie.get('popularity'), vote_count=movie.get('vote_count'),
                vote_average=movie.get('vote_average'),
                )
            movie_instance.save()
            # 장르 가져와서 연결하는 로직
            genres = movie.get('genre_ids')
            for genre in genres:
                genre_instance = get_object_or_404(Genre, pk=genre)
                movie_instance.genres.add(genre_instance)
    movie_list = get_list_or_404(Movie)
    serializer = MovieListSerializer(movie_list, many=True)
    # return Response로 통일
    return Response(serializer.data, status=status.HTTP_200_OK)
            
# 장르 저장 로직
@api_view(['GET'])
def getgenres(request):
    URL = 'https://api.themoviedb.org/3/genre/movie/list?api_key=4507744d222eb5c01174a9eb93bdf2af'
    response = requests.get(URL)
    for genre in response.json().get('genres'):
        genre = Genre(id=genre.get('id'), name=genre.get('name'))
        genre.save()
    genre_list = get_list_or_404(Genre)
    serializer = GenreSerializer(genre_list, many=True)
    # print(Response(serializer.data))
    # return Response로 통일해줌.
    return Response(serializer.data, status=status.HTTP_200_OK)

# 영화 정보 받아서 뿌리기위한 로직
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def showmovies(request):
    # Movie List를 db에서 가져오고 없으면 404를 반환
    movie_list = get_list_or_404(Movie)
    # MovieListSerializer로 Movie 모델에서 데이터를 읽은 후 모든 필드에서 직렬화를 통해 json으로 변환
    serializer = MovieListSerializer(movie_list, many=True)
    # HTTP status 코드와 함께 반환
    return Response(serializer.data, status=status.HTTP_200_OK)


# 영화 정보 받아서 뿌리기위한 로직
@api_view(['GET'])
def test(request):
    # 정참조
    movie = Movie.objects.get(pk=8)
    prefer_users = movie.prefer_users.all()
    serializer = UserSerializer(prefer_users, many=True)

    # # 중개모델 쿼리
    # prefer = Prefer.objects.get(movie=8)
    # serializer = PreferSerializer(prefer)

    # # 역참조
    # user = User.objects.get(pk=6)
    # prefer_movies = user.prefer_movies.all()
    # serializer = MovieSerializer(prefer_movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

