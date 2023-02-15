pipeline {
    agent any

    stages {
        stage('clone github repo') {
                steps {
                    git 'https://github.com/raoufcherfa/employe.git'
                }
            }

       stage('install env') {
            steps {
                sh 'pip install --no-cache-dir -r requirements.txt'
            }
        }

        stage('build python app') {
            steps {
                sh 'python app.py'
            }
        }

        stage('tests unitaires') {
                steps {
                    sh 'pytest unit_tests.py'
                }
            }
    }
}
