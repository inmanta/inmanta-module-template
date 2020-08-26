pipeline {
    agent any
    options {
        disableConcurrentBuilds()
        skipDefaultCheckout()
    }
    stages {
        stage("initialize module and setup virtualenv") {
            dir('inmanta-module-template') {
                checkout scm
            }
            dir('module') {
                sh '''
                    python3 -m ${WORKSPACE}/venv env
                    ${WORKSPACE}/env/bin/pip install -U pip cookiecutter
                    cookiecutter --no-input ../inmanta-module-template/
                    ${WORKSPACE}/env/bin/pip install -r requirements.txt -r requirements.dev.txt
                '''
            }
        }
        stage("tests") {
            steps {
                dir('module/test_module') {
                    sh '''
                        ${WORKSPACE}/env/bin/pytest tests -v -s --junitxml=junit.xml
                        junit 'junit.xml'
                    '''
                }
            }
        }
        stage("code linting") {
            steps {
                dir('module/test_module') {
                    sh '${WORKSPACE}/env/bin/flake8 plugins tests'
                }
            }
        }
    }
}
