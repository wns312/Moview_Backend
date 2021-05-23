from django.urls import path
from . import views
urlpatterns = [
    # articles/id/movie/id
    path('movie/<int:movie_id>/', views.articles),
    path('<int:article_id>/movie/<int:movie_id>/', views.article_detail)
]
