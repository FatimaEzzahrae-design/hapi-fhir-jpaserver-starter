pipeline {
    agent any

    stages {
        stage('Checkout Code') {
    steps {
        git url: 'https://github.com/FatimaEzzahrae-design/hapi-fhir-jpaserver-starter.git', 
            branch: 'master', 
            credentialsId: 'github-pat'
    }
}

        stage('Build Project') {
    steps {
        script {
            def mvnHome = tool name: 'Maven3', type: 'maven'
            bat "\"${mvnHome}\\bin\\mvn\" clean package -DskipTests"
        }
    }
}

stage('Run Tests') {
    steps {
        script {
            def mvnHome = tool name: 'Maven3', type: 'maven'
            bat "\"${mvnHome}\\bin\\mvn\" test"
        }
    }
}

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t fatimaezahraafras/hapi-fhir-jpaserver:latest .'
            }
        }

    }
}
