pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/saumil1400/stockk'
            }
        }

        stage('Use Minikube Docker') {
            steps {
                sh "eval \$(minikube docker-env)"
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t streamlit-app:latest ."
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh "kubectl apply -f k8s/"
            }
        }

        stage('Restart Pod') {
            steps {
                sh "kubectl delete pod -l app=streamlit || true"
            }
        }
    }
}
