pipeline {
    agent any
    
    parameters {
        string(
            name: 'VERSION',
            defaultValue: '1.0',
            description: 'Kaunsa version deploy karna hai?'
        )
        choice(
            name: 'ENVIRONMENT',
            choices: ['Development', 'Staging', 'Production'],
            description: 'Kahan deploy karna hai?'
        )
        booleanParam(
            name: 'RUN_TESTS',
            defaultValue: true,
            description: 'Tests run karne hain?'
        )
    }
    
    environment {
        DEVELOPER = "Chetan Padaliya"
        APP_NAME = "Jenkins Parameters Project"
    }
    
    stages {
        
        stage('Checkout') {
            steps {
                echo "Developer: ${DEVELOPER}"
                echo "Version: ${params.VERSION}"
                echo "Environment: ${params.ENVIRONMENT}"
                echo "Tests chalenge: ${params.RUN_TESTS}"
            }
        }
        
        stage('Build') {
            steps {
                echo "Building version ${params.VERSION}..."
                echo "Build complete!"
            }
        }
        
        stage('Test') {
            when {
                expression { params.RUN_TESTS == true }
            }
            steps {
                echo "Tests run ho rahe hain..."
                echo "Sab tests pass!"
            }
        }
        
        stage('Deploy') {
            steps {
                echo "Deploying ${APP_NAME}..."
                echo "Version ${params.VERSION} → ${params.ENVIRONMENT}"
                
                script {
                    if (params.ENVIRONMENT == 'Production') {
                        echo "⚠️ PRODUCTION PE DEPLOY HO RAHA HAI!"
                    } else {
                        echo "✅ ${params.ENVIRONMENT} pe deploy hua!"
                    }
                }
            }
        }
        
    }
    
    post {
        success {
            echo "✅ ${APP_NAME} v${params.VERSION} → ${params.ENVIRONMENT} SUCCESS!"
        }
        failure {
            echo "❌ Deploy fail hua!"
        }
    }
}