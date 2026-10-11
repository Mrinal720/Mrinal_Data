pipeline {
    agent any
    
    stages{
        stage('Build'){
            steps{
              echo "build completed successfully"
            }
        }

        stage('Test'){
            steps{
              echo "Test completed successfully"
            }
        }
        stage('Package'){
            steps{
              echo "package completed successfully"
            }
        }

        stage('Deploy'){
            steps{
              echo "deploy completed successfully"
            }
        }
    }
}
//     environment {
//         PIPENV_VENV_IN_PROJECT = '1'
//     }

//     stages {
//         stage('Checkout') {
//             steps {
//                 checkout scm
//             }
//         }
//         stage('Install dependencies') {
//             steps {
//                 sh 'pip install --user pipenv'
//                 sh 'pipenv install --dev'
//             }
//         }
//         stage('Unit tests') {
//             steps {
//                 sh 'pipenv run pytest --junitxml=reports/junit.xml'
//             }
//             post {
//                 always {
//                     junit 'reports/junit.xml'
//                 }
//             }
//         }
//         stage('Smoke run') {
//             steps {
//                 sh 'pipenv run python application_main.py LOCAL'
//             }
//         }
//     }
// }
