pipeline {
    agent any

    environment {
        PIPENV_VENV_IN_PROJECT = '1'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Install dependencies') {
            steps {
                sh 'pip install --user pipenv'
                sh 'pipenv install --dev'
            }
        }
        stage('Unit tests') {
            steps {
                sh 'pipenv run pytest --junitxml=reports/junit.xml'
            }
            post {
                always {
                    junit 'reports/junit.xml'
                }
            }
        }
        stage('Smoke run') {
            steps {
                sh 'pipenv run python application_main.py LOCAL'
            }
        }
    }
}
