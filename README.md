# 1학기 최종 프로젝트 보일러플레이트

## 멤버 - 김준영, 한건


## 진행 상황


### 공통

[ ✔ ] 패키지 설치

[ ✔ ] gitignore 설정

[ ❌ ] License 추가

[ ❌ ] author 추가


### Back-End

[ ✔ ]  User 모델 작성

[ ✔ ] User model에서 email을 필수로 받도록 수정

[ ✔ ]  UserSerializer 작성

[ ✔ ] CORS 정책 전체 허용으로 변경

[ ✔ ]  JWT 설정 및 jwt토큰 발급 url 설정

[ ✔ ]  signup 로직 구현

...
[  ] 초기 추천 완료. 이제 로그인 시 is_recommended에 따라 추천을 받을지 안받을지 구현하고, is_recommended 튕겨내기 작성 + is_recommended가 false일 시 다른 페이지에 접근할 수 없도록 설정

[  ] views.py Http Method 이상한 곳 수정하기

[  ] 별점 가중치를 -6~4?

0 1 2 3 4 5 6 7 8 9 10

-4 -3 -2 -2 -1 -1 0 1 2 3 4 (6까지는 선호한다고 보기 어렵기 때문)

[  ] 관리자 페이지 구성을 위한 질문 (admin.py 구성)




## Back-End 서버 패키지

``django ``
``django-seed ``
``django-cors-headers ``
``djangorestframework ``
``djangorestframework-jwt``





