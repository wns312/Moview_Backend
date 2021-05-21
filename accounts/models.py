from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Movie
# Create your models here.
class User(AbstractUser):
    # 필드 정의
    # 이 필드를 통해 영화 id를 가져와서 장르를 취합 한 뒤, 보내주고 이후 state에서 관리
    # 영화 선호 추가시 state와 id추가를 각자 해줘서 DB 접근 최소화
    # 영화 선호 목록 추가 기준은 더 고민해볼것
    prefer_movies = models.ManyToManyField(Movie, related_name='prefer_users')
    # False일 시 선호영화 선택 페이지를 로그인 시 띄우고 True만듬
    is_recommended = models.BooleanField(default=False)  

    # 필드 재정의
    email = models.EmailField(max_length=150, unique=True)
    # 유저이름 필드를 email로 변경하겠다
    USERNAME_FIELD = 'email'
    # createsuperuser 커맨드로 유저를 생성할 때 나타날 필드 이름 목록
    # USERNAME_FIELD로 지정된 필드는 REQUIRED_FIELDS에서 제외되어야 한다고 한다.
    # 따라서 email은 REQUIRED_FIELDS에서 제외되어야 한다. (자동으로 나온다)
    # username은 포함되어야 한다.
    REQUIRED_FIELDS = ('username', 'password')

    def __str__(self):
      return self.email
