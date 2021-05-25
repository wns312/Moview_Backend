from django.shortcuts import render, get_object_or_404, get_list_or_404
from datetime import date
import requests
# models
from .models import Movie, Genre, Prefer
from accounts.models import User
# drf
from rest_framework import status
from rest_framework.response import Response
from accounts.serializers import UserSerializer, UserUpdateSerializer
from .serializers import GenreSerializer, MovieSerializer, MovieListSerializer, PreferSerializer, PreferSaveSerializer, PreferRecommendSerializer
# jwt
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
# Create your views here.

@api_view(['POST', 'PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def movie_vote(request, movie_id):
    
    if request.method == 'DELETE':
        prefer = get_object_or_404(Prefer, movie_id=movie_id, user=request.user)
        prefer.delete()
        return Response({'Success' : True})

    rating = request.data.get('rating')
    # 유효한 숫자가 아닐 경우 리턴시킨다.
    if not 0 <= rating <= 10 or type(rating) != type(int(rating)):
        return Response({'message' : '유효한 숫자가 아닙니다'}, status=status.HTTP_400_BAD_REQUEST)
    request.data['user'], request.data['movie'] = request.user.id, movie_id
    is_prefer_exist = Prefer.objects.filter(movie_id=movie_id, user=request.user).exists()
    if request.method == 'POST' and not is_prefer_exist:
        serializer = PreferSaveSerializer(data=request.data)
    else:  # PUT일 경우
        prefer = get_object_or_404(Prefer, movie_id=movie_id, user=request.user)
        serializer = PreferSaveSerializer(prefer, data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
    

@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def get_movie_detail(request, movie_id):
    is_prefer_exist = Prefer.objects.filter(movie_id=movie_id, user=request.user).exists()
    if is_prefer_exist:
        # Movie 기준으로 가져오는게 아니라 prefer 기준으로 PreferSerializer에 movie를 정의해놓아야 하는 것
        prefer = get_object_or_404(Prefer.objects.select_related('movie'), movie_id=movie_id, user=request.user)
        serializer = MovieSerializer(prefer.movie)
        return Response({"movie" : serializer.data, "rating" : prefer.rating})
    else :
        movie = get_object_or_404(Movie, pk=movie_id)
        serializer = MovieSerializer(movie)
        return Response({"movie" : serializer.data, "rating" : None})



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
def showmovies(request):
    # Movie List를 db에서 가져오고 없으면 404를 반환
    movie_list = get_list_or_404(Movie)
    # MovieListSerializer로 Movie 모델에서 데이터를 읽은 후 모든 필드에서 직렬화를 통해 json으로 변환
    serializer = MovieListSerializer(movie_list, many=True)
    # HTTP status 코드와 함께 반환
    return Response(serializer.data, status=status.HTTP_200_OK)






def return_genres(datas):
    count_dict = {
        12: [0, 'Adventure', 12], 14: [0, 'Fantasy', 14], 16: [0, 'Animation', 16], 18: [0, 'Drama', 18], 
        27: [0, 'Horror', 27], 28: [0, 'Action', 28], 35: [0, 'Comedy', 35], 36: [0, 'History', 36], 
        37: [0, 'Western', 37], 53: [0, 'Thriller', 53], 80: [0, 'Crime', 80], 99: [0, 'Documentary', 99], 
        878: [0, 'Science Fiction', 878], 9648: [0, 'Mystery', 9648], 10402: [0, 'Music', 10402], 10749: [0, 'Romance', 10749], 
        10751: [0, 'Family', 10751], 10752: [0, 'War', 10752], 10770: [0, 'TV Movie', 10770]
    }
    for data in datas:
        genres = data.get("movie").get('genres')
        for genre in genres:
            count_dict[genre][0] = count_dict[genre][0]+1
    prior = list(count_dict.values())
    prior.sort(reverse=True)
    return prior[:3]


# 영화 정보 받아서 뿌리기위한 로직
@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def recommend(request):
    if request.method == 'GET':
        # 없을 경우 404 에러와 함께 나오는 메시지 { "detail": "찾을 수 없습니다." }
        prefers = Prefer.objects.select_related('movie').filter(rating__gte=8, user_id=request.user.id)
        prefers = get_list_or_404(prefers)
        serializer = PreferRecommendSerializer(prefers, many=True)
        genres = return_genres(serializer.data)
        recommended_movies = dict()
        for c, genre, genreNum in genres:
            movies = get_list_or_404(Movie.objects.order_by('popularity'), genres=genreNum)[:20]
            recommended_movies.setdefault(genre, list())
            serializer = MovieListSerializer(movies, many=True)
            recommended_movies[genre] = serializer.data
        return Response(recommended_movies, status=status.HTTP_200_OK)
    else:  # POST
        movies = request.data
        for movie in movies:
            movie['user'] = request.user.id
            serializer = PreferSaveSerializer(data=movie)
            # 중복처리 해줘야 함 -> 안해줘도 됨. 왜냐면 첫 로그인 때만 가능하게 할 거니까
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            
        # 이제 유저의 is_recommended 를 true로 만들어주고 저장해준다.
        serializer = UserUpdateSerializer(request.user, data={ 'is_recommended' : True})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(movies)




