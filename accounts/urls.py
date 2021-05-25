from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token
urlpatterns = [
    path('signup/', views.signup),
    path('userinfo/', views.user_info),
    path('api-token-auth/', obtain_jwt_token),
]
