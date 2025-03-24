### 명령어 설명

```
python manage.py runserver # 디버깅에서만 사용
python manage.py makemigrations # 새 모델 추가 혹은 모델 필드 변경 사항 있을 경우
python manage.py migrate # 위의 경우에 기존 마이그레이션을 데이터 베이스에 적용 혹은 샤ㅐ로운 데이터 베이스에서 기존 마이그레이션을 적용할 경우
```

### Third-Part Package

```
pip install django
pip install djangorestframework
pip install django-filter
pip install Pillow // File Transfer
pip install psycopg2-binary // Tag => ArrayField
pip install psycopg // Tag => ArrayField
```

### migrations 에러 해결 예시

django.db.utils.ProgrammingError: column "category" of relation "posts_post" does not exist
새로운 필드를 추가하였는데 반영이 안됨

#### 1. PostgreSQL에서 해당 필드확인

```
psql -U johnhan -h 127.0.0.1 -d myblog
\d posts_post;
```

#### 2. 자동으로 모델의 새로운 필드를 인식 못한 경우라 수동으로 작업해줘야함

```
python manage.py makemigrations --empty posts
```

후에 파일 변경 사항 직접 migration해주기

### AWS EC2 접근하기

```
chmod 400 your-key.pem
ssh -i your-key.pem username@server-i
```
