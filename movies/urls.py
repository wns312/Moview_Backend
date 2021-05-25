from django.urls import path
from . import views
urlpatterns = [
    path('<int:movie_id>/', views.get_movie_detail),
    path('<int:movie_id>/vote', views.movie_vote),
    path('getmovies/', views.getmovies),
    path('getgenres/', views.getgenres),
    # 영화 정보 뿌려주기 위해 임시로
    path('showmovies/', views.showmovies),
    path('recommend/', views.recommend)
]
