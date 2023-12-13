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
                    sh '''
                        # follow README instructions exactly
                        python3 -m venv .env && source .env/bin/activate
                        pip install -r requirements.txt -r requirements.dev.txt
                        pip install -e .
                    '''
                }
            }
        }
        stage("tests") {
            steps {
                dir('module/test-module') {
                    sh '.env/bin/pytest tests -v -s --junitxml=junit.xml'
                }
            }
        }
        stage("code linting") {
            steps {
                dir('module/test-module') {
                    sh '.env/bin/flake8 inmanta_plugins tests'
                }
            }
        }
    }
    post{
        cleanup{
            deleteDir()
        }
    }
}
