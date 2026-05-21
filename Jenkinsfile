pipeline {
    agent any

    stages {
        stage('Code Checkout') {
            steps {
                echo 'Pulling the latest codebase from version control...'
            }
        }

        stage('Docker Image Build') {
            steps {
                echo 'Compiling Dockerfile blueprint into a fresh app container...'
                bat 'docker build -t devops-shop-app .'
            }
        }

        stage('Container Deployment') {
            steps {
                echo 'Cleaning up old instances and launching the new application container...'
                bat 'docker rm -f running-shop-container 2>nul || exit 0'
                bat 'docker run -d -p 4000:4000 --name running-shop-container devops-shop-app'
                echo 'Waiting for application initialization...'

                //This replaces the broken Windows timeout command cleanly
                sleep time: 5, unit: 'SECONDS'
            }
        }

        stage('Selenium Verification') {
            steps {
                echo 'Executing headless Selenium verification tests against port 4000...'
                bat 'python test.py'
            }
        }
    }
}
