pipeline {
    agent any
    environment {
        FLASK_APP = "app.py"
        FLASK_ENV = "development"
    }
    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: 'master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/raoufcherfa/employe.git']]])
            }
        }
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
        stage('Run API') {
            steps {
                sh 'python app.py &'
            }
        }
        stage('Test API') {
            steps {
                sh 'pytest unit_tests.py'
            }
        }
        stage('Merge to Dev') {
            steps {
                sh 'git checkout Dev && git merge master'
            }
        }
        stage('Deploy to Dev') {
            steps {
                sh 'fab deploy_dev'
            }
        }
    }
}
