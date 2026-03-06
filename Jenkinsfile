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

        stage('SonarQube Analysis') {
    steps {
        withSonarQubeEnv('SonarQubeLocal') { // Nom défini dans Jenkins SonarQube server
            script {
                def mvnHome = tool name: 'Maven3', type: 'maven'
                bat "\"${mvnHome}\\bin\\mvn\" sonar:sonar -Dsonar.projectKey=hapi-fhir-jpaserver -Dsonar.host.url=http://localhost:9000 -Dsonar.login=sqa_9e331f3efa2f8a1cb5beefe3ea613f5409c8b949"
            }
        }
    }
}

    }
}
