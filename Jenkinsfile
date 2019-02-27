pipeline {
    agent {
        docker { image 'node:8.11' }
    }
    stages {
        stage('Install dependencies') {
            steps {
                sh 'yarn install'
            }
        }
    }
}