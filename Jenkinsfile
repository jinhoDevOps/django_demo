// Jenkinsfile

pipeline {
    agent any  // Jenkins가 이 파이프라인을 어느 에이전트에서 실행할지 정의합니다. 'any'는 임의의 에이전트에서 실행됨을 의미합니다.

    // 환경 변수 설정
    environment {
        DJANGO_SETTINGS_MODULE = 'django_demo.settings'
        MY_DB_HOST = 'mysql.db.com:192.168.123.163'
    }

    triggers {
        pollSCM('H/2 * * * *')  // 2분마다 SCM을 체크하여 변화가 있으면 빌드를 트리거합니다.
    }

    stages {
        stage('Checkout from GitHub') {  // GitHub에서 코드를 체크아웃하는 단계
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[url: 'https://github.com/jinhoDevOps/django_demo.git']]])
            }
        }

        // pip3 install --no-cache-dir -r requirements.txt 대신 직접명시
        stage('Install Python Dependencies') {  // 파이썬 의존성을 설치하는 단계
            steps {
                sh '''
                apt install -y python3 python3-pip python3-venv pkg-config default-libmysqlclient-dev
                python3 -m venv myenv
                . myenv/bin/activate
                pip install Django==4.2.4 djangorestframework==3.14.0 mysqlclient==2.2.0
                '''
            }
        }

        stage('Run Unit Tests') {  // 유닛 테스트를 실행하는 단계
            steps {
                        // 가상 환경을 활성화합니다. / Django 테스트를 실행합니다.
                sh '''
                . myenv/bin/activate
                python manage.py test
                '''
            }
        }

        stage('Build Docker Image') {  // 도커 이미지를 빌드하는 단계
            steps {
                sh 'docker build -t django_demo .'  // 도커 이미지를 빌드합니다.
            }
        }

        stage('Deploy to Docker Container') {  // 도커 컨테이너에 배포하는 단계
                steps {
                sh '''
                docker stop django_demo || true
                docker rm django_demo || true
                docker run -d -p 8000:8000 --add-host $MY_DB_HOST --name django django_demo 
                '''
            }
        }
    }
}
