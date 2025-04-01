### 명령어 설명

```bash
python manage.py runserver # 디버깅에서만 사용
python manage.py makemigrations # 새 모델 추가 혹은 모델 필드 변경 사항 있을 경우
python manage.py migrate # 위의 경우에 기존 마이그레이션을 데이터 베이스에 적용 혹은 샤ㅐ로운 데이터 베이스에서 기존 마이그레이션을 적용할 경우
```

### Third-Part Package

사용된 패키지들은 requirements.txt를 참고합니다.

```bash
pip freeze
pip install -r requirements.txt
```

### migrations 에러 해결 예시

django.db.utils.ProgrammingError: column "category" of relation "posts_post" does not exist
새로운 필드를 추가하였는데 반영이 안됨

#### 1. PostgreSQL에서 해당 필드확인

```bash
psql -U johnhan -h 127.0.0.1 -d myblog
\d posts_post;
```

#### 2. 자동으로 모델의 새로운 필드를 인식 못한 경우라 수동으로 작업해줘야함

```bash
python manage.py makemigrations --empty posts
```

후에 파일 변경 사항 직접 migration해주기

### AWS EC2 접근하기

```bash
chmod 400 your-key.pem
ssh -i your-key.pem username@server-i

# 서버 PostgreSQL 설정
sudo apt update
sudo apt install postgresql postgresql-contrib

# Ngix 및 Gunicorn 설정
# systemd에 새 서비스 적용
sudo systemctl daemon-reload

# 서비스 실행
sudo systemctl start gunicorn

# 부팅 시 자동 시작
sudo systemctl enable gunicorn

# 상태 확인
sudo systemctl status gunicorn
```

### 코드 업데이트 후 (pull)

```bash
sudo systemctl restart gunicorn # guinicorn 재시작
sudo systemctl restart nginx # nginx 설정 바꾸면 역시 재시작
```
