pipeline {
    agent any

    environment {
        REPOSITORY_URL = 'https://github.com/JeanGrendel/TrabalhoDevOps-RA-2397305.git'
        BRANCH_NAME = 'main'
    }

    stages {
        stage('Trazer código do Git') {
            steps {
                // Clonar o repositório do Git
                git branch: "${BRANCH_NAME}", url: "${REPOSITORY_URL}"
            }
        }

        stage('Build e Deploy') {
            steps {
                script {
                    // Construir as imagens Docker para cada serviço
                    sh '''
                        docker compose build
                    '''

                    // Subir os containers do Docker com Docker Compose
                    sh '''
                        docker compose up -d
                    '''
                }
            }
        }

        stage('Rodar Testes') {
            steps {
                script {
                    // Rodar os testes com o pytest (ou qualquer outra ferramenta de testes que você esteja utilizando)
                    sh 'sleep 40' 
                    sh 'docker compose run --rm test'
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline executada com sucesso!'
        }
        failure {
            echo 'A pipeline falhou.'
        }
    }
}
