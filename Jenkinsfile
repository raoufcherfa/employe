pipeline {
    agent any

    stages {
        stage('clone github repo') {
                steps {
                    git 'https://github.com/raoufcherfa/employe.git'
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
