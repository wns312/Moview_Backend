from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
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
