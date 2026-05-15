pipeline {
    agent any
    
    parameters {
        choice(
            name: 'ENVIRONMENT',
            choices: ['Development', 'Staging', 'Production'],
            description: 'Kahan deploy karna hai?'
        )
        booleanParam(
            name: 'SIMULATE_FAILURE',
            defaultValue: false,
            description: 'Failure test karni hai?'
        )
    }
    
    environment {
        DEVELOPER = "Chetan Padaliya"
        APP_NAME = "Jenkins Error Handling"
    }
    
    stages {
        
        stage('Checkout') {
            steps {
                echo "Developer: ${DEVELOPER}"
                echo "Environment: ${params.ENVIRONMENT}"
            }
        }
        
        stage('Build') {
            steps {
                timeout(time: 1, unit: 'MINUTES') {
                    echo "Build shuru..."
                    echo "Build complete!"
                }
            }
        }
        
        stage('Test') {
            steps {
                retry(3) {
                    echo "Tests run ho rahe hain..."
                    
                    script {
                        if (params.SIMULATE_FAILURE) {
                            error "TEST FAIL! Simulate kiya!"
                        }
                    }
                    
                    echo "Sab tests pass!"
                }
            }
        }
        
        stage('Deploy') {
            steps {
                script {
                    try {
                        echo "Deploy ho raha hai..."
                        
                        if (params.ENVIRONMENT == 'Production') {
                            echo "⚠️ Production deploy - extra check!"
                        }
                        
                        echo "Deploy successful!"
                        
                    } catch (Exception e) {
                        echo "❌ Deploy fail hua: ${e.getMessage()}"
                        currentBuild.result = 'FAILURE'
                        throw e
                    }
                }
            }
        }
        
    }
    
    post {
        success {
            echo "✅ ${APP_NAME} → ${params.ENVIRONMENT} SUCCESS!"
        }
        failure {
            echo "❌ PIPELINE FAIL! Team ko batao!"
            echo "Developer: ${DEVELOPER} check karo!"
        }
        always {
            echo "Pipeline khatam - Result: ${currentBuild.result}"
        }
    }
}