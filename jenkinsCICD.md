# Jenkins CI/CD Test Guide for Django Project

## 필요한 사전 조건
- Jenkins가 설치된 서버 (도커로 실행 가능)
- GitHub 레포지토리에 장고 프로젝트가 저장되어 있어야 함 (테스트 프로젝트)

## Jenkinsfile 생성

1. 프로젝트 루트 디렉토리에 `Jenkinsfile`을 생성합니다.
2. 아래의 예시 코드를 `Jenkinsfile`에 붙여넣습니다.

```groovy
pipeline {
    agent any

    environment {
        DJANGO_SETTINGS_MODULE = 'django_demo.settings'
    }

    triggers {
        pollSCM('H/5 * * * *')
    }

    stages {
        stage('Checkout from GitHub') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[url: 'https://github.com/jinhoDevOps/django_demo.git']]])
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh 'python manage.py test'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t django_demo .'
            }
        }

        stage('Deploy to Docker Container') {
            steps {
                sh 'docker run -d -p 8000:8000 django_demo'
            }
        }
    }
}
```

## Jenkins 설정

1. Jenkins 웹 UI에 접속합니다. (http://[your-server-ip]:9090)
2. 'New Item'을 클릭합니다.
3. 이름을 입력하고 'Pipeline'을 선택한 후, 'OK'를 클릭합니다.
4. 이후 설정에서 'Pipeline' 섹션으로 스크롤합니다.
5. 'Definition'을 'Pipeline script from SCM'으로 설정합니다.
6. 'SCM'을 'Git'으로 선택합니다.
7. 'Repository URL'에 GitHub 레포지토리의 URL`https://github.com/jinhoDevOps/django_demo.git`을 입력합니다.
8. 'Save'를 클릭합니다.

이렇게 설정하면 Jenkins가 5분마다 GitHub 레포지토리를 체크하여 변경 사항이 있으면 자동으로 파이프라인을 실행합니다.

## Jenkins 빌드 오류
```bash
hudson.plugins.git.GitException: Command "git fetch --tags --force --progress --prune -- origin +refs/heads/master:refs/remotes/origin/master" returned status code 128:
stdout: 
stderr: fatal: couldn't find remote ref refs/heads/master

	at org.jenkinsci.plugins.gitclient.CliGitAPIImpl.launchCommandIn(CliGitAPIImpl.java:2842)
	at org.jenkinsci.plugins.gitclient.CliGitAPIImpl.launchCommandWithCredentials(CliGitAPIImpl.java:2185)
	at org.jenkinsci.plugins.gitclient.CliGitAPIImpl$1.execute(CliGitAPIImpl.java:635)
	at jenkins.plugins.git.GitSCMFileSystem$BuilderImpl.build(GitSCMFileSystem.java:406)
	at jenkins.scm.api.SCMFileSystem.of(SCMFileSystem.java:219)
	at org.jenkinsci.plugins.workflow.cps.CpsScmFlowDefinition.create(CpsScmFlowDefinition.java:118)
	at org.jenkinsci.plugins.workflow.cps.CpsScmFlowDefinition.create(CpsScmFlowDefinition.java:70)
	at org.jenkinsci.plugins.workflow.job.WorkflowRun.run(WorkflowRun.java:311)
	at hudson.model.ResourceController.execute(ResourceController.java:101)
	at hudson.model.Executor.run(Executor.java:442)
Finished: FAILURE
```
Jenkins가 Git 레포지토리에서 `master` 브랜치를 찾을 수 없다고 에러 메시지가 나타나고 있습니다. 이 문제는 일반적으로 다음과 같은 경우에 발생할 수 있습니다:

1. 레포지토리에 `master` 브랜치가 없을 때: GitHub는 최근에 기본 브랜치 이름을 `main`으로 변경했습니다. 레포지토리의 기본 브랜치가 `main`인지 확인해 보세요.

2. 권한 문제: Jenkins가 레포지토리에 액세스할 수 있는지 확인해야 합니다.


### 브랜치 설정 오류

- **문제**: 'Branches to build'를 비워두면 'any'가 기본값으로 적용되어 'master' 브랜치가 빌드됩니다. 만약 'master' 브랜치가 없다면 빌드가 실패합니다.
- **해결 방법**: 'Branches to build'에 빌드하려는 브랜치의 이름을 명시적으로 입력합니다.

### 의존성 누락 오류

- **문제**: Jenkins가 실행되는 컨테이너에 필요한 의존성(예: Python)이 없을 경우 빌드가 실패합니다.
- **해결 방법**: Dockerfile이나 Jenkinsfile에서 필요한 의존성을 설치하는 단계를 추가합니다.

예: Dockerfile에 파이썬 설치 추가

```Dockerfile
# ... (기존 코드)

# Install Python3 and pip
RUN apt install -y python3 python3-pip

# ... (기존 코드)
```

또는 Jenkinsfile에서 파이썬 설치 단계 추가

```groovy
stage('Install Dependencies') {
    steps {
        sh 'apt install -y python3 python3-pip'  // Linux 패키지 의존성을 설치합니다.
        sh 'pip install -r requirements.txt'  // 파이썬 의존성을 설치합니다.
    }
}
```

이렇게 하면 필요한 의존성을 컨테이너에 설치하여 빌드 오류를 해결할 수 있습니다.
## 빌드 트리거

- Jenkins 설정에서 'Poll SCM'을 선택하고, 스케줄을 `H/5 * * * *`로 설정합니다. 이렇게 하면 5분마다 GitHub 레포지토리를 체크합니다.

## 빌드 및 배포 모니터링

- Jenkins 대시보드에서 빌드 및 배포 상태를 모니터링할 수 있습니다.

