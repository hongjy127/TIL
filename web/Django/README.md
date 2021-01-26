# Django

## HTTP 프로토콜

1. connect
2. request
   - 요청 라인 (1줄)
   - 요청 헤더 (n줄, 항목 1개당 1줄)
     - key, value로 이루어짐
     - view의 request 객체가 받는 정보
     - GET, POST
   - 요청 본체
3. response
   - 상태 라인 (1출)
   - 응답 헤더 (n줄)
     - 주요 상태코드
       - 200 : ok
       - 40x : 요청이 잘못됨(client 잘못)
       - 50x : 서버 잘못 
   - 응답 본체
4. close



- WEB 서버 / WAS

- URL



## 프로그램 만들기

프로젝트 경로에서 cmd창 열어주기

- 가상환경

    ```
    $ conda create -n 가상환경이름
    $ conda activate 가상환경이름
    ```

- 장고 설치
    ```
    $ pip install Django
    ```

- 패키지 설치

  ```
MariaDB 사용 시
  $ conda install mysqlclient
  ```
  
- 데이터베이스 만들기

  ```mariadb
  MariaDB 명령창에서 해도 되고 Heidi에서 해도 되고
  CREATE DATABASE db이름;
  CREATE USER '사용자ID'@'%' IDENTIFIED BY '비밀번호';
  GRANT ALL PRIVILEGES ON db이름.* TO '사용자ID'@'%';
  ```

- 프로젝트 만들기

  설정과 관련된 이름을 쓰기 위해 프로젝트 이름이 아닌 mysite로 만들고 나중에 파일 이름을 바꿔줌

  폴더가 생김 (mysite/settings.py, urls.py 사용)

    ```
  $ django-admin startproject mysite
  $ ren mysite 프로젝트 이름
    ```


- setting

  app/mysite/settings.py

  ```python
  # 추가/변경할 것들
  
  #
  ALLOWED_HOST = []
  
  # 앱 등록
  INSTALLED_APPS = [
  	'앱이름'
  ]
  
  # 템플릿 설정
  TEMPLATES = [
      ...
      'DIRS': [
          # 템플릿 찾을 디렉토리 추가
          os.path.join(BASE_DIR, 'templates')
      ],
  ]
  
  # 데이터베이스
  DATABASE = {
      ...
      # sql 사용
      'ENGINE': 'django.db.backends.sqlite3'
      
      # MariaDB 사용
      'ENGINE': 'django.db.backends.mysql',
      'NAME': '데이터베이스명',
      'HOST': 'localhost',
      'PORT': '3306',
      'USER': '사용자ID',
      'PASSWORD': '비밀번호'
  }
  
  # 정적 파일 설정
  STATIC_URL = '/static/'
  
  # 타임존, 언어 설정
  LANGUAGE_CODE = 'ko-kr'
  TIME_ZONE = 'Asia/Seoul'
  
  # 개발환경
  DEBUG=TRUE : 개발환경
  ```

- 기본 테이블 생성

  모델을 기반으로 해서 데이터베이스의 테이블 만들어줌 (실제 db 반영)

  ````
  $ python manage.py migrate
  -> Heidi에서 추가된 것을 볼 수 있음.
  ````

- 슈퍼유저 만들기

  데이터베이스마다 존재함

  ```
  $ python manage.py createsuperuser
  -> name, address, pw 설정
  ```

- 웹 서버 기동

  ```
  $ python manage.py runserver [포트번호]
  -> admin페이지로 로그인 가능 (127.0.0.1/admin)
  ```


- 앱 만들기

    폴더가 생김 (앱폴더/admin.py models.py views.py urls.py 사용)

    ```
    $ python managy.py startapp 앱폴더 이름
    ```



1. models.py, admin.py : 테이블 관련

   데이터베이스 변경 반영

   ```
   전체[해당 앱]에대해 조사
   $ python manage.py makemigrations [앱이름]
   모델을 기반으로 해서 데이터베이스의 테이블 만들어줌 (실제 db 반영)
   $ python manage.py migrate
   ```

2. URLconf - urls.py : URL과 view 관계

3. views.py

4. templates/ .html, 화면 UI



### models.py

```python
# 테이블 생성
from django.db import models

class 모델클래스(models.Model):
    # id는 자동 생성 (PK)
    컬럼명 = models.CharField(max_length= )	# varchar
    models.IntegerField()
    models.DateTimeField()
    models.ForeignKey()	# on_delete=models.CASCADE: 부모가 삭제될 때 같이 삭제
    models.ManyToManyField(모델명)	# 모델이 이후에 정의된다면 문자열로 넣어야함.
    
# 리턴값
objects.all() : 전체
choice(모델클래스)_set.all() : PK, FK로 연결된 행만
```

### admin.py

```python
# 127.0.0.1/admin에서 볼 수 있게 함.
from 앱이름.models import 모델클래스

admin.site.register(모델클래스)
```

```python
# 일부만 출력한다면
from 앱이름.models import 모델클래스

@admin.register(모델클래스)
class 모델명Admin(admin.ModelAdmin):
    list_display = ('컬럼명', '컬럼명')	# 사이트에서 출력할 컬럼 목록 ()
```



### urls.py / views.py

- 함수형 views.py (FBV)
  - urls.py

    ```python
    # view 이름 중복을 막기위해 app별로 구성함
    # 앱이름/urls.py
    from django.urls import path
    from 앱이름 import views

    app_name = '앱이름'

    # 변수명은 꼭 urlpatterns로
    urlpatterns = [
        # 기본경로는 /앱이름/
        path('', views.index, name='index')
        # /앱이름/여기가 바뀜
        path('<경로변수 - view에서>/', views.함수, name='뷰이름')
        # path('<int:question_id>/', views.detail, name='detail')
    ]
    ```

  - mysite/urls.py

      ```python
      # mysite/urls.py 에 추가해주기
      from django.contrib import admin
      from django.urls import path, include

      urlpatterns = [
          path('admin/', admin.site.urls),
          path('앱이름/', include('앱이름(패키지명).urls'))
      ]
      ```

  - views.py

    ```python
    from django.shortcuts import render
    from 앱이름.models import 모델명
    
    def index(request):
        # html을 만들기 전에는 pass로 두고 만들기
        # pass
    
        인스턴스 = 모델클래스.objects.all().order_by()
        
        # context 변수 (상황변수)
        context = 
    return render(request, 'html 경로', context)
      
      def detail(request, <경로변수>와 동일)
      ...
      
      get_object_or_404(모델클래스, pk=)	# 존재하면 모 인스턴스, 아니면 404에러
    ```




- 클래스형 views.py (CBV) - FBV보다 많이 쓰임

  - urls.py

    ```python
    # view 이름 중복을 막기위해 app별로 구성함
    # 앱이름/urls.py
    from django.urls import path
    from 앱이름 import views

    app_name = '앱이름'

    # 변수명은 꼭 urlpatterns로
    urlpatterns = [
        path('<경로변수>/', views.클래스.as_view(), name='detail')
        # path('<int:pk>/', views.DetailView.as_view(), name='detail')
    ]
    ```
  
- views.py

  - [참고](https://github.com/django/django/tree/master/django/views/generic)

  ```python
  from django.shortcuts import render
    
  from django.views.generic import ListView, DetailView
  from 앱이름.models import 모델명
  
  # TemplateView
  class 모델명(TemplateView):
      template_name = 
      def get_context_data(self, **kwargs):
          context = super.get_context_data(**kwargs)
          context['model_list'] = ['모델클래스']
          return context
  
  class 모델명(ListView):
      model = Bookmark
      # object_list : ListView에서 넘겨주는 context 변수
      # 템플릿 경로: 앱이름/templates/앱이름/모델명_list.html
  
  class 모델명(DetailView):
      model = Bookmark   
      # object : DetailView에서 넘겨주는 context 변수
      # 템플릿 경로: 앱이름/templates/앱이름/모델명_detail.html
  ```

#### 제너릭뷰

- TemplateView : 뷰 템플릿을 직접 제어할 때
- ListView : 목록 보기
- DetailView : 한 개 상세보기






### templates/ / .html

- 템플릿 명 규칙 : 모델명(소문자)\_list.html, 모델명(소문자)_detail.html

- 디폴트명이 싫으면 views.py에서

  `template_name = 'books/b_list.html'` 이런 식으로 정의하기



insert, update, delete는 항상 redirect 해주기



## 데이터 조작 (shell 이용)

```
설정이 적용된 파이썬 환경이 구축
>>> python manage.py shell
```

- Create

```
>>> from polls.models import Question, Choice
>>> from django.utils import timezone
>>> q = Question(question_text = "What's new?", pub_date=timezone.now()) 
>>> q.save()
```

- Read
  - 모든 모델은 objects(매니저, 쿼리셋) 속성을 가짐
  - `all()`, `get()`, `filter_by()`, `filter()`, `exclude()`

- Update
  - 단일 레코드 수정: 필드 수정 후 save() 호출
  - 다중 레코드 수정: 모델 객체에서 필터링한 뒤 update() 호출
- Delete
  - `delete()`



## template

### 템플릿 변수

- {{표현식}}
  - 값을 출력
- . 연산자 처리 절차(예시 - foo.bar)
  - foo가 사전인지 확인 --> foo['bar']
  - 사전이 아닌 경우 속성 확인 --> foo.bar
  - 리스트인지 확인 --> foo[bar]
- 정의 되지 않은 변수는 ' '로 처리



### 템플릿 필터

- {{ 표현식 | 필터명 }}
  - linebreaks
  - default



### 템플릿 태그

- {% tag %}
- {% for %}
  - 들여쓰기로 코드블럭을 지정할 수 없음
  -  {% for %}{% endfor %}
  - forloop
    - forloop.count : 현재까지 루프를 실행한 루프 카운트
    - forloop.first, forloop.last

- {% if %}

  ```
  {% if %}
  
  {% elif %}
  
  {% else %}
  
  {% endif%}
  ```

- {% csrf_token %}

  - `<form>{% csrf_token %}`
  - CSRF 공격 방지
  - 실패 시 403 에러
  ```html
  <form>
  # form 쓸 땐 보안을 위해 반드시 넣어줌
  {% csrf_token %}
  </form>
  ```


- {% url %}

  - 하드코딩 방지
  - `{% url '네임스페이스:뷰이름' [파라미터] %}`
  - 파이썬 코드(뷰 함수 내)에서는 reverse()와 같은 역할

- {% with %}
  - 객체 안에 객체를 쓸 때
  - 대입문, as 모두 사용 가능



### 템플릿 주석

- 단일 라인 주석: {#  #}
- 여러 줄 주석: {% comment %}



### 템플릿 상속

- templates/base.html : 프로젝트 전체에 사용
- templates/base_앱이름.html : 앱마다 사용



- 경로변수 \<데이터타입(변환함수명):변수명>로 표기







