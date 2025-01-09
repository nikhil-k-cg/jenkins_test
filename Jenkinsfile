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
        
        // stage ('flask install'){
        //         steps {
        //         sh 'sudo apt install -y python3-flask'
        //         }
        // }
        // stage ('Pytest install'){
        //         steps {
        //         sh "sudo apt install -y python3-pytest"
        //         }
        // }
        stage('Build Image') {
            steps {
                script {
                    img = IMAGE_NAME + ":${env.BUILD_ID}"
                    println ("${img}")
                    //dockerImage = docker.build("${img}")
                    def dockerImage = docker.build("${IMAGE_NAME}:${TAG}")
                    // "docker build -t ${img} ."
                }
            }
        }
        // stage ('Test'){
        //         steps {
        //         sh "pytest testroutes.py"
        //         }
        // }
        
        // stage ('Clean Up'){
        //     steps{
        //         sh returnStatus: true, script: 'docker stop $(docker ps -a | grep ${JOB_NAME} | awk \'{print $1}\')'
        //         sh returnStatus: true, script: 'docker rmi $(docker images | grep ${registry} | awk \'{print $3}\') --force' //this will delete all images
        //         sh returnStatus: true, script: 'docker rm ${JOB_NAME}'
        //     }
        // }

        // stage('Build Image') {
        //     steps {
        //         script {
        //             img = registry + ":${env.BUILD_ID}"
        //             println ("${img}")
        //             dockerImage = docker.build("${img}")
        //         }
        //     }
        // }

        // stage('Push To DockerHub') {
        //     steps {
        //         script {
        //             // docker.withRegistry( 'https://registry.hub.docker.com ', registryCredential ) {
        //             //     dockerImage.push()
        //             docker.withRegistry("${REGISTRY}", "${registryCredential}") {
        //                 dockerImage.push()
        //             }
        //         }
        //     }
        // }
                    
        stage('Deploy') {
           steps {
                sh label: '', script: "docker run -d --name ${JOB_NAME} -p 5000:5000 ${img}"
          }
        }

      }
    }
