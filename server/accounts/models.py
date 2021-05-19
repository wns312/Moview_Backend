from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    # 필드 재정의
    email = models.EmailField(
      max_length=150,
      help_text = 'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
      error_messages = {
        'unique': "A user with that username already exists.",
      },
      unique=True
    )
    # 유저이름 필드를 email로 변경하겠다
    USERNAME_FIELD = 'email'
    # 유저이름 필드가 email이므로, 필요 필드에 username과 password를 적는 것
    REQUIRED_FIELDS = ('username', 'password')

    def __str__(self):
      return self.email
