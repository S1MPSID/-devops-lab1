pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m pip install --user -r requirements.txt'
            }
        }

        stage('Lint') {
            steps {
                sh 'python3 -m flake8 app.py'
            }
        }

        stage('Unit Tests') {
            steps {
                sh 'python3 -m pytest test_app.py -v'
            }
        }

        stage('Package') {
            steps {
                sh 'tar -czf devops-lab1-${BUILD_NUMBER}.tar.gz app.py test_app.py requirements.txt'
            }
        }
    }

    post {
        success {
            echo 'Build, lint, tests and packaging completed successfully.'
        }

        failure {
            echo 'Pipeline failed.'
        }
    }
}