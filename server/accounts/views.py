from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


from .serializers import UserSerializer


@api_view(['GET', 'POST'])
def signup(request):
  user = get_object_or_404(get_user_model(), pk=1)
  serializer = UserSerializer(user)
  return Response(serializer.data)