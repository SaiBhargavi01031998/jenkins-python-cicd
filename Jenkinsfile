pipeline {
    agent any

    environment {
        DEPLOY_DIR = '/opt/python-app'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Validate') {
            steps {
                sh 'python3 --version'
                sh 'git --version'
                sh 'ls -l'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m unittest -v test_app.py'
            }
        }

        stage('Build') {
            steps {
                sh '''
                    mkdir -p dist
                    cp app.py dist/app.py
                    echo "Build artifact created"
                    ls -l dist/
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    mkdir -p "$DEPLOY_DIR"
                    cp dist/app.py "$DEPLOY_DIR/app.py"
                    echo "Application copied to deployment directory"
                '''
            }
        }

        stage('Verify') {
            steps {
                sh 'python3 "$DEPLOY_DIR/app.py"'
            }
        }
    }

    post {
        success {
            echo 'CI/CD pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check Console Output.'
        }
        always {
            echo 'Pipeline execution finished.'
        }
    }
}
