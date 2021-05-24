from django.urls import path
from . import views
urlpatterns = [
    # 모든 articles를 보여주는 기본 url
    path('', views.articles),
    # 'post' / article CREATE url
    path('movie/<int:movie_id>/', views.movie_article),
    # 미구현
    path('<int:article_id>/movie/<int:movie_id>/', views.article_detail)
]
