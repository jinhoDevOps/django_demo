# django_demo

이 Django 데모 프로젝트는 Python 기반의 웹 애플리케이션 프레임워크인 Django를 사용하고 있습니다.  
Django의 이름은 유명 재즈 기타리스트 Django Reinhardt에서 따온 것으로, 그의 다재다능성과 유연성을 상징합니다.

* [스프링 프로젝트 변환 가이드](./아무튼스크립트.md)
* [젠킨스 관련 메모](./jenkinsREADME.md)

## 사전 작업 - secrets.py 파일 생성

Django 프로젝트에 민감한 정보를 안전하게 저장하기 위해 `secrets.py` 파일을 사용할 수 있습니다.

- `secrets.py` 파일은 `settings.py` 파일과 같은 디렉토리(`django_demo/`)에 위치해야 합니다.

### 변수 예시

```python
# secrets.py
SECRET_KEY = 'your-secret-key-here'
DEBUG = True or False
DB_PASSWORD = 'your-database-password'
DB_HOST = 'your-database-host'
DB_PORT = 'your-database-port'
```

주의사항

- 이 파일은 `.gitignore`에 추가하여 버전 관리 시스템(Git 등)에 포함되지 않도록 해야 합니다.
- 실제 배포 시에는 `DEBUG` 값을 `False`로 설정해야 보안을 강화할 수 있습니다.

이렇게 설정한 후 `settings.py` 파일에서 `from .secrets import *` 문을 추가하여 이 변수들을 사용할 수 있습니다. - 추가되어있음

