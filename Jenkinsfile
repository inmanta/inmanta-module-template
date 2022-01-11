pipeline {
    agent any
    triggers{
        cron(BRANCH_NAME == "master" ? "H H(2-5) * * *": "")
    }
    options {
        disableConcurrentBuilds()
        skipDefaultCheckout()
    }
    stages {
        stage("initialize module and setup virtualenv") {
            steps {
                deleteDir()
                dir('inmanta-module-template') {
                    checkout scm
                }
                dir('module') {
                    sh '''
                        python3 -m venv ${WORKSPACE}/env
                        ${WORKSPACE}/env/bin/pip install -U pip cookiecutter
                        ${WORKSPACE}/env/bin/cookiecutter --no-input ../inmanta-module-template/
                    '''
                }
                dir('module/test-module') {
                    sh '${WORKSPACE}/env/bin/pip install -r requirements.txt -r requirements.dev.txt'
                }
            }
        }
        stage("tests") {
            steps {
                dir('module/test-module') {
                    sh '${WORKSPACE}/env/bin/pytest tests -v -s --junitxml=junit.xml'
                }
            }
        }
        stage("code linting") {
            steps {
                dir('module/test-module') {
                    sh '${WORKSPACE}/env/bin/flake8 plugins tests'
                }
            }
        }
    }
}
