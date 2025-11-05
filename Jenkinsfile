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
                        uv tool run cookiecutter --no-input ../inmanta-module-template/
                    '''
                }
                dir('module/test-module') {
                    sh '''
                        python_version=$(curl https://docs.inmanta.com/community/latest/reference/compatibility.json | jq -r '.system_requirements.python_version')
                        uv venv --python "$python_version"
                        uv pip install pip
                        source .venv/bin/activate
                        # follow README instructions exactly, except for Python version
                        pip install -e . -c requirements.txt -r requirements.dev.txt
                    '''
                }
            }
        }
        stage("tests") {
            steps {
                dir('module/test-module') {
                    sh '.venv/bin/pytest tests -v -s --junitxml=junit.xml'
                }
            }
        }
        stage("code linting") {
            steps {
                dir('module/test-module') {
                    sh '.venv/bin/flake8 inmanta_plugins tests'
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
