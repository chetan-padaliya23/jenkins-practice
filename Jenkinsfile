pipeline {
    agent any
    
    environment {
        DEVELOPER = "Chetan Padaliya"
        APP_NAME = "Chetan Ka Calculator"
        PYTHON = "\"C:\\Program Files\\Python312\\python.exe\""
    }
    
    stages {
        
        stage('Checkout') {
            steps {
                echo "========================================="
                echo "Code GitHub se aa raha hai..."
                echo "Developer: ${DEVELOPER}"
                echo "App: ${APP_NAME}"
                echo "========================================="
            }
        }
        
        stage('Install Dependencies') {
            steps {
                echo "Dependencies install ho rahi hain..."
                bat "${PYTHON} -m pip install -r requirements.txt"
                echo "Dependencies install ho gayi!"
            }
        }
        
        stage('Run Tests') {
            steps {
                echo "Tests run ho rahe hain..."
                bat "${PYTHON} test_app.py"
                echo "Saare tests pass ho gaye!"
            }
        }
        
        stage('Run App') {
            steps {
                echo "App run ho rahi hai..."
                bat "${PYTHON} app.py"
            }
        }
        
        stage('Deploy') {
            steps {
                echo "========================================="
                echo "${APP_NAME} successfully deploy hua!"
                echo "Production ready hai!"
                echo "========================================="
            }
        }
        
    }
    
    post {
        success {
            echo "SUCCESS! ${APP_NAME} - Pipeline complete!"
            echo "Chetan bhai ne real project deploy kiya!"
        }
        failure {
            echo "FAILED! Pipeline fail hui - Check karo!"
        }
        always {
            echo "Build complete: ${currentBuild.result}"
        }
    }
}