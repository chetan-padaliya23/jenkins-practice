pipeline {
    agent any
    
    environment {
        DEVELOPER = "Chetan Padaliya"
        APP_NAME = "Jenkins GitHub Project"
    }
    
    stages {
        
        stage('Checkout') {
            steps {
                echo "Code GitHub se aaya!"
                echo "Developer: ${DEVELOPER}"
            }
        }
        
        stage('Build') {
            steps {
                echo "Build ho raha hai..."
                echo "Code compile hua!"
            }
        }
        
        stage('Test') {
            steps {
                echo "Tests run ho rahe hain..."
                echo "Sab tests pass!"
            }
        }
        
        stage('Deploy') {
            steps {
                echo "${APP_NAME} deploy ho gaya!"
            }
        }
        
    }
    
    post {
        success {
            echo "✅ GitHub se pipeline SUCCESS!"
        }
        failure {
            echo "❌ Kuch gadbad hai, dekho!"
        }
    }
}
