def img
pipeline {
    environment {
        // registry = "nikhil1289/jenkins_test" //To push an image to Docker Hub, you must first name your local image using your Docker Hub username and the repository name that you created through Docker Hub on the web.
        REGISTRY = 'https://registry.hub.docker.com'
        IMAGE_NAME = 'nikhil1289/jenkins_test'      
        registryCredential = 'DOCKERHUB'
        githubCredential = 'GITHUB'
        dockerImage = ''
    }
    agent any
    stages {
        stage('checkout') {
            steps {
                git branch: 'master',
                credentialsId: githubCredential,
                url: 'https://github.com/nikhil-k-cg/jenkins_test.git'
            }
        }
        stage('Build Image') {
            steps {
                script {
                    img = IMAGE_NAME + ":${env.BUILD_ID}"
                    println ("${img}")
                    //dockerImage = docker.build("${img}")
                    // def dockerImage = docker.build("${IMAGE_NAME}:${TAG}")
                    sh "docker build -t ${img} ."
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                script {
                    // Push the Docker image to Docker Hub
                    sh "docker push ${img} "
                    }
                }
            }
        }       
        stage('Deploy') {
            steps {
                sh label: '', script: "docker run -d --name ${JOB_NAME} -p 5000:5000 ${img}"
            }
        }
    }
}