pipeline {
    agent any

    stages {
        stage('clone github repo') {
                steps {
                    git 'https://github.com/raoufcherfa/employe.git'
                }
            }
        stage('install docker') {
                steps {
                    sh '''
                            # Download the Docker installation script
                            curl -fsSL https://get.docker.com -o get-docker.sh

                            # Run the Docker installation script with sudo privileges
                            sudo sh get-docker.sh
                        '''
                }
            }
        stage('Docker build') {
            steps {
                sh 'docker build -t employe:1.0 .'
            }
        }
        stage('Docker run') {
            steps {
                sh 'docker run -d -p 8081:8081 employe:1.0 --name=container_employe'
            }
        }
        stage('tests unitaires') {
                steps {
                    sh 'docker exec container_employe bash -c "pytest unit_tests.py"'
                }
            }
    }
}
