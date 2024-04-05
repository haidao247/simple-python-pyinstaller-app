pipeline {
    agent any 
    stages {
        stage('publish info') {
            steps {
                echo "start building"
            }
        }
        stage('Build') { 
            steps {
                echo "this is PR number ${env.CHANGE_ID}"
                sh 'python3 sources/read.py' 
            }
        }
        stage('Deliver') {
            steps {
                echo 'Finishinggggg'
            }
        }
    }
}
