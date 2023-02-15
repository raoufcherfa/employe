pipeline {
    agent any
    environment {
        FLASK_APP = "app.py"
        FLASK_ENV = "development"
    }
    stages {
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'pytest'
            }
        }
        stage('Deploy') {
            steps {
                sh 'python app.py'
            }
        }
    }
}
