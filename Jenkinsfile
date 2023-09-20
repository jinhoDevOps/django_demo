// Jenkinsfile

pipeline {
    agent any  // Jenkins가 이 파이프라인을 어느 에이전트에서 실행할지 정의합니다. 'any'는 임의의 에이전트에서 실행됨을 의미합니다.

    // 환경 변수 설정
    environment {
        DJANGO_SETTINGS_MODULE = 'django_demo.settings'
    }

    triggers {
        pollSCM('H/5 * * * *')  // 5분마다 SCM을 체크하여 변화가 있으면 빌드를 트리거합니다.
    }

    stages {
        stage('Checkout from GitHub') {  // GitHub에서 코드를 체크아웃하는 단계
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[url: 'https://github.com/jinhoDevOps/django_demo.git']]])
            }
        }

        stage('Install Dependencies') {  // 의존성을 설치하는 단계
            steps {
                sh 'pip install -r requirements.txt'  // 파이썬 의존성을 설치합니다.
            }
        }

        stage('Run Unit Tests') {  // 유닛 테스트를 실행하는 단계
            steps {
                sh 'python manage.py test'  // Django 테스트를 실행합니다.
            }
        }

        stage('Build Docker Image') {  // 도커 이미지를 빌드하는 단계
            steps {
                sh 'docker build -t django_demo .'  // 도커 이미지를 빌드합니다.
            }
        }

        stage('Deploy to Docker Container') {  // 도커 컨테이너에 배포하는 단계
            steps {
                sh 'docker run -d -p 8000:8000 django_demo'  // 도커 컨테이너를 실행합니다.
            }
        }
    }
}
