pipeline {
    agent any

    environment {
        DOCKER_CREDENTIALS = credentials('dockerhub')  // Must match Jenkins credentials ID
        DOCKER_IMAGE = "yemisi76/devops-django:latest"
    }

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/Yemmmyc/devops-django-project.git', branch: 'main'
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
    }

    post {
        success {
            echo 'Build and push completed successfully.'
        }
        failure {
            echo 'Build failed.'
        }
    }
}
