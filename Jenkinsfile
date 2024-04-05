pipeline {
    agent any 
    stages {
        stage
        stage('Build') { 
            steps {
                echo "this is PR number ${CHANGE_ID}"
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
