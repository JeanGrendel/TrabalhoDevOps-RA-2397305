pipeline {
    agent any

    environment {
        COMPOSE_FILE = 'docker-compose.yml'
    }

    stages {
        stage('Build') {
            steps {
                sh '''
                    docker compose down
                    docker compose up --build -d
                    docker compose ps
                '''
            }
        }

        stage('Wait for Flask') {
            steps {
                script {
                    def isReady = false
                    for (int i = 0; i < 30; i++) { // 30 tentativas (30 segundos)
                        try {
                            sh 'curl --fail -X GET http://localhost:5000/alunos'
                            isReady = true
                            break
                        } catch (Exception e) {
                            echo "Tentativa ${i + 1} de 30 para verificar se o Flask está pronto..."
                            sleep(1) // Aguarda 1 segundo antes de tentar novamente
                        }
                    }
                    if (!isReady) {
                        error "Servidor Flask não iniciou a tempo!"
                    }
                }
            }
        }

        stage('Test') {
            steps {
                sh '''
                    echo "Testando GET /alunos"
                    curl -s -o /dev/null -w "%{http_code}" -X GET http://localhost:5000/alunos || exit 1

                    echo "Testando POST /alunos"
                    curl -s -o /dev/null -w "%{http_code}" -X POST http://localhost:5000/alunos \
                    -H "Content-Type: application/json" \
                    -d '{
                        "nome": "Teste",
                        "sobrenome": "Teste",
                        "turma": "Teste",
                        "disciplinas": "Teste1, Teste2"
                    }' || exit 1
                '''
            }
        }
    }
}
