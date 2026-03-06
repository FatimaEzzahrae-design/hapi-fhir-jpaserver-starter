pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "fatimaezahraafras/hapi-fhir-jpaserver:latest"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/FatimaEzzahrae-design/hapi-fhir-jpaserver-starter.git'
            }
        }

        stage('Build Project') {
            steps {
                sh 'mvn clean package -DskipTests'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'mvn test'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }

        stage('Push Docker Image') {
            steps {
                sh 'docker push $DOCKER_IMAGE'
            }
        }

        stage('Deploy Kubernetes') {
            steps {
                sh 'kubectl apply -f k8s/deployment.yml'
                sh 'kubectl apply -f k8s/service.yml'
            }
        }

    }
}