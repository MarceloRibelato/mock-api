// Common paramenters
def CLIENT = "brinks"
def AWS_CLIENT_ID = "373686486237"
def ECR_BRINKS_REGION = "sa-east-1"
def ECR_MATERA_REGION = "us-east-1"
//def ECR_REPOSITORY = "${AWS_CLIENT_ID}.dkr.ecr.us-east-1.amazonaws.com"
def DOCKER_IMAGE_NAME = "mock-partner-transaction"
def DOCKER_SOCKET = "/var/run/docker.sock:/var/run/docker.sock"

def ECR_REPOSITORY(aws_region) {
    return "373686486237.dkr.ecr.${aws_region}.amazonaws.com"
}

// Begin build pipeline
pipeline {
    options { timeout(time: 1, unit: 'HOURS') }
    triggers { pollSCM('H */5 * * 1-5') }
    agent { label 'docker' }
    stages {
        // Mock
        stage('Mock'){
            agent { label 'docker' }
            stages {
                stage('Build') {
                    steps {
                        sh script: "docker build -t ${ECR_REPOSITORY(ECR_MATERA_REGION)}/${DOCKER_IMAGE_NAME}:latest .", label: "Build container start process"
                    }
                }
                stage('Configure') {
                    steps {
                    script {
                            if (env.BRANCH_NAME == 'master'){
                                sh script: "docker tag ${ECR_REPOSITORY(ECR_MATERA_REGION)}/${DOCKER_IMAGE_NAME}:latest ${ECR_REPOSITORY(ECR_BRINKS_REGION)}/${DOCKER_IMAGE_NAME}:latest", label: "Tag gateway image with latest tag - BRINKS"
                                sh script: "docker tag ${ECR_REPOSITORY(ECR_MATERA_REGION)}/${DOCKER_IMAGE_NAME}:latest ${ECR_REPOSITORY(ECR_BRINKS_REGION)}/${DOCKER_IMAGE_NAME}:${GIT_COMMIT}", label: "Tag gateway image with git commit - BRINKS"
                                sh script: "docker tag ${ECR_REPOSITORY(ECR_MATERA_REGION)}/${DOCKER_IMAGE_NAME}:latest ${ECR_REPOSITORY(ECR_MATERA_REGION)}/${DOCKER_IMAGE_NAME}:${GIT_COMMIT}", label: "Tag gateway image with git commit - MATERA"
                            }
                            else{
                                sh script: "docker tag ${ECR_REPOSITORY(ECR_MATERA_REGION)}/${DOCKER_IMAGE_NAME}:latest ${ECR_REPOSITORY(ECR_MATERA_REGION)}/${DOCKER_IMAGE_NAME}:\$(echo '${env.BRANCH_NAME}' | sed 's|/|-|g')", label: "Tag image with branch name - MATERA"
                            }
                        }
                    }
                }
                stage('Push to MATERA_REGION') {
                    steps {
                        withCredentials([usernamePassword(credentialsId: 'aws.brinks.jenkins', usernameVariable: 'AWS_ACCESS_KEY_ID', passwordVariable: 'AWS_SECRET_ACCESS_KEY')]) {
                                sh script: "AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID} AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY}  \$(aws ecr get-login --no-include-email --region ${ECR_MATERA_REGION})", label: "Login in ECR repository"
                        }
                        script {
                            if (env.BRANCH_NAME == 'master'){
                                sh script: "docker push ${ECR_REPOSITORY(ECR_MATERA_REGION)}/${DOCKER_IMAGE_NAME}:latest", label: "Push latest gateway docker image"
                                sh script: "docker push ${ECR_REPOSITORY(ECR_MATERA_REGION)}/${DOCKER_IMAGE_NAME}:${GIT_COMMIT}", label: "Push tagged gateway docker image"
                            }
                            else{
                                sh script: "docker push ${ECR_REPOSITORY(ECR_MATERA_REGION)}/${DOCKER_IMAGE_NAME}:\$(echo '${env.BRANCH_NAME}' | sed 's|/|-|g')", label: "Push gateway docker image with branch name"
                            }
                        }
                    }
                }
            }
        }
    }
}
