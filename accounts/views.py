from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


from .serializers import UserSerializer


@api_view(['GET', 'POST'])
def signup(request):
  print(request.data)
  # 1. 비밀번호와 비밀번호 확인이 일치하는지 확인한다.
  password = request.data.get('password')
  password_confirm = request.data.get('passwordConfirm')
  if password != password_confirm : 
    # 이렇게 쓴 이유는 isvalid에서 튕겨져 나오는 형식을 맞춰주기 위함임
    return Response({"passwordConfirm" : {"비밀번호 확인이 일치하지 않습니다"}}, status=status.HTTP_400_BAD_REQUEST) 

  # 2. serializer로 받아서 저장을 한다. 그리고 결과로 serializer의 data를 리턴한다.
  serializer = UserSerializer(data=request.data)
  if serializer.is_valid(raise_exception=True):
    user = serializer.save()
    user.set_password(request.data.get('password'))
    user.save()
    return Response(serializer.data)

  return Response()