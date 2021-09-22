pipeline {
    environment {
        registry = "maximelau/test_project"
        registryCredential = 'goeland040695'
    } 
    
    agent any
    stages {
        stage('Cloning Git') {
            steps {
                git 'https://github.com/zuper-meh/Crash_projet'
            }
        }
        stage('Building image') {
            steps {
                script {
                    sh '''cd /var/lib/jenkins/workspace/docker_build_test'''
                    sh '''docker build --tag "$registry:latest" --tag "$registry:$BUILD_NUMBER" .'''
                }
            }
        }
        stage('Deploy Image') {
            steps {
                script {
                    sh '''docker login -u maximelau -p $registryCredential'''
                    sh '''docker push -a $registry'''
                    sh '''docker logout'''
                }
            }
        }
        stage('Remove Unused docker image') {
            steps {
                sh "docker rmi $registry:$BUILD_NUMBER"
                sh "docker rmi $registry:latest"
            }
        }
        stage('Créer le venv') {
            steps {
                withPythonEnv('python3') {
                    sh '''pip install -r requirements.txt'''
                    sh '''pytest'''
                }
            }
        }
        stage("nétoyer l'espace de travail") {
            steps {
                sh '''cd $WORKSPACE'''
                sh '''rm -rf ./test'''
            }
        }
        stage('Save the build') {
            steps {
                sh ''' mkdir -p /home/maximel/Desktop/savesJenkinsBuild '''
                sh ''' tar cvfz /home/maximel/Desktop/savesJenkinsBuild/$JOB_NAME-$BUILD_NUMBER.tar .'''
            }
        }
    }
}
