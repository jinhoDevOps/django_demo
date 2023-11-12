# 베이스 이미지를 설정합니다.
FROM python:3.11.2

# 작업 디렉토리를 설정합니다.
WORKDIR /app

# 의존성 파일을 복사합니다.
COPY requirements.txt .

# 의존성을 설치합니다.
RUN pip install --no-cache-dir -r requirements.txt

# 모든 파일을 복사합니다.
COPY . .

# 8000포트를 엽니다
EXPOSE 8000

# 서버를 실행합니다.
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]