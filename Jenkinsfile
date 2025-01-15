// def img
// pipeline {
//     environment {
//         // registry = "nikhil1289/jenkins_test" //To push an image to Docker Hub, you must first name your local image using your Docker Hub username and the repository name that you created through Docker Hub on the web.
//         REGISTRY = 'https://registry.hub.docker.com'
//         IMAGE_NAME = 'nikhil1289/jenkins_test'      
//         registryCredential = 'DOCKERHUB'
//         githubCredential = 'GITHUB'
//         dockerImage = ''
//     }
//     agent any
//     stages {
//         stage('checkout') {
//             steps {
//                 git branch: 'master',
//                 credentialsId: githubCredential,
//                 url: 'https://github.com/nikhil-k-cg/jenkins_test.git'
//             }
//         }
//         stage('Build Image') {
//             steps {
//                 script {
//                     img = IMAGE_NAME + ":${env.BUILD_ID}"
//                     println ("${img}")
//                     //dockerImage = docker.build("${img}")
//                     // def dockerImage = docker.build("${IMAGE_NAME}:${TAG}")
//                     sh "docker build -t ${img} ."
//                 }
//             }
//         }
//         stage('Push Docker Image') {
//             steps {
//                 script {
//                     // Push the Docker image to Docker Hub
//                     sh "docker push ${img} "
//                 }
//             }
//         }       
//         stage('Deploy') {
//             steps {
//                 sh label: '', script: "docker run -d --name ${JOB_NAME} -p 5000:5000 ${img}"
//             }
//         }
//     }
// }
pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'nikhil1289/jenkins_test'
        DOCKER_REGISTRY = 'docker.io' // Default registry (Docker Hub)
        DOCKER_CREDENTIALS_ID = 'DOCKERHUB' // Jenkins credentials ID for Docker registry credentials
        githubCredential = 'GITHUB'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master',
                credentialsId: githubCredential,
                url: 'https://github.com/nikhil-k-cg/jenkins_test.git'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image
                    sh 'docker build -t $DOCKER_IMAGE:$BUILD_NUMBER .'
                }
            }
        }

        stage('Login to Docker Registry') {
            steps {
                script {
                    //docker.withRegistry("$DOCKER_REGISTRY", "$DOCKER_CREDENTIALS_ID") {
                        // Login to Docker registry
                         withCredentials([usernamePassword(credentialsId: DOCKER_CREDENTIALS_ID, usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        sh '''
                            echo $DOCKER_PASSWORD | docker login $DOCKER_REGISTRY -u $DOCKER_USERNAME --password-stdin
                        '''
                    }
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    // Push the Docker image to the registry
                    // docker.withRegistry("$DOCKER_REGISTRY", "$DOCKER_CREDENTIALS_ID") {
                    //     sh "docker push $DOCKER_IMAGE:$BUILD_NUMBER"
                    // }
                    sh "docker push $DOCKER_IMAGE:$BUILD_NUMBER"
                }
            }
        }
        
        stage('Docker run') {
            steps{
                script {
                    sh "docker run -d -p 5000:5000 $DOCKER_IMAGE:$BUILD_NUMBER"
                }
            }
        }
    }

    post {
        success {
            echo 'Docker image built and pushed successfully!'
        }
        failure {
            echo 'Build or push failed!'
        }
    }
}
