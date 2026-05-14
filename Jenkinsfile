pipeline {
    agent any
    
    environment {
        DEVELOPER = "Chetan Padaliya"
        APP_NAME = "Jenkins GitHub Project"
        VERSION = "4.0"
    }
    
    stages {
        
        stage('Checkout') {
            steps {
                echo "Code GitHub se aaya!"
                echo "Developer: ${DEVELOPER}"
                echo "Version: ${VERSION}"
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
                echo "${APP_NAME} v${VERSION} deploy ho gaya!"
            }
        }
        
    }
    
    post {
        success {
            echo "✅ VSCode se likha, GitHub pe push kiya, Jenkins ne run kiya!"
        }
        failure {
            echo "❌ Kuch gadbad hai!"
        }
    }
}