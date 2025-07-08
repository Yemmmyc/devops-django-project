pipeline {
    agent any

    environment {
        DOCKER_CREDENTIALS = credentials('dockerhub')  // Jenkins credentials ID
        DOCKER_IMAGE = "yemisi76/devops-django:latest"
    }

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/Yemmmyc/devops-django-project.git', branch: 'master'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image: ${DOCKER_IMAGE}"
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }

        stage('Push Docker Image') {
            steps {
                echo "Pushing Docker image to DockerHub..."
                sh 'echo $DOCKER_CREDENTIALS_PSW | docker login -u $DOCKER_CREDENTIALS_USR --password-stdin'
                sh 'docker push $DOCKER_IMAGE'
            }
        }

        stage('Run with Docker Compose') {
            steps {
                echo "Running app using Docker Compose with remote image..."
                sh 'docker-compose down || true'  // Stop old containers if running
                sh 'docker-compose pull'
                sh 'docker-compose up -d --build'
            }
        }
    }

    post {
        success {
            echo '✅ Build, push, and run completed successfully.'
        }
        failure {
            echo '❌ Build failed.'
        }
    }
}
