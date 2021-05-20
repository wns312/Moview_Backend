from django.urls import path
from . import views
urlpatterns = [
    path('getmovies/', views.getmovies),
    path('getgenres/', views.getgenres),
]
