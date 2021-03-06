from django.urls import path
from . import views
urlpatterns = [
    # 모든 articles를 보여주는 기본 url
    path('', views.articles),
    # 'get', 'post' / article CREATE url
    path('movie/<int:movie_id>/', views.movie_article),
    # 'get / put / delete'
    path('<int:article_id>/', views.article_detail),

    # get / post / delete 
    path('<int:article_id>/comments/', views.article_comment),

]
