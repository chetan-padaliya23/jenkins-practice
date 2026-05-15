pipeline {
    agent any
    
    environment {
        DEVELOPER = "Chetan Padaliya"
        APP_NAME = "Jenkins Credentials Project"
        VERSION = "5.0"
        DB_PASS = credentials('db-password')
        MY_API  = credentials('api-key')
    }
    
    stages {
        
        stage('Checkout') {
            steps {
                echo "Developer: ${DEVELOPER}"
                echo "Version: ${VERSION}"
            }
        }
        
        stage('Build') {
            steps {
                echo "Build ho raha hai..."
                echo "Database connect ho raha hai..."
                echo "DB Password hai: ${DB_PASS}"
                echo "Build complete!"
            }
        }
        
        stage('Test') {
            steps {
                echo "API se connect ho raha hai..."
                echo "API Key hai: ${MY_API}"
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
            echo "✅ Credentials safely use hue!"
        }
        failure {
            echo "❌ Kuch gadbad hai!"
        }
    }
}