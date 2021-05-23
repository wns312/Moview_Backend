from django.urls import path
from . import views
urlpatterns = [
    # articles/id/movie/id
    path('movie/<int:movie_id>/article/', views.articles),
    path('movie/<int:movie_id>/article/<int:article_id>/', views.article_detail)
]
