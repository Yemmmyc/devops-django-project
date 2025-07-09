pipeline {
    agent any

    environment {
        DOCKER_CREDENTIALS = credentials('dockerhub')     // Jenkins credentials ID
        IMAGE_NAME = "yemisi76/devops-django"
        IMAGE_TAG = "latest"
        DEPLOYMENT_NAME = "django-app"
        CONTAINER_NAME = "django-app"
    }

    stages {
        stage('Checkout') {
            steps {
                echo "🔄 Cloning repository from GitHub..."
                git url: 'https://github.com/Yemmmyc/devops-django-project.git', branch: 'main'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "🔧 Building Docker image: ${IMAGE_NAME}:${IMAGE_TAG}"
                sh 'docker build -t $IMAGE_NAME:$IMAGE_TAG .'
            }
        }

        stage('Push Docker Image') {
            steps {
                echo "📤 Pushing Docker image to Docker Hub..."
                sh 'echo $DOCKER_CREDENTIALS_PSW | docker login -u $DOCKER_CREDENTIALS_USR --password-stdin'
                sh 'docker push $IMAGE_NAME:$IMAGE_TAG'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo "🚀 Updating Kubernetes deployment..."
                sh '''
                    kubectl set image deployment/$DEPLOYMENT_NAME $CONTAINER_NAME=$IMAGE_NAME:$IMAGE_TAG --record
                    kubectl rollout status deployment/$DEPLOYMENT_NAME
                '''
            }
        }
    }

    post {
        success {
            echo '✅ CI/CD Pipeline completed successfully!'
        }
        failure {
            echo '❌ CI/CD Pipeline failed.'
        }
    }
}
