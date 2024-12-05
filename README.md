-- Trabalho de DevOps --
#Monitoramento de Aplicação Flask com Grafana, Prometheus e Jenkins
Nome: Jean Carlos Brito Grendel RA: 23.9730-5


Este projeto configura um ambiente monitorado para uma aplicação Flask utilizando ferramentas como Grafana, Prometheus e Jenkins. As instruções abaixo guiam você no processo de configuração, execução e uso das ferramentas integradas.

#Pré-requisitos
Para iniciar, verifique se possui as seguintes ferramentas instaladas:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Postman](https://www.postman.com/)
- [Git](https://git-scm.com/)
- [Jenkins](https://www.jenkins.io/) (opcional para pipelines)

-

#Clonar o projeto:
1. Clone este repositório:
   ```bash
   git clone https://github.com/JeanGrendel/TrabalhoDevOps-RA-23.9730-5.git
   ```
   Os: Antes de iniciar os conainers, finalize todos os containers  imagens ja existentes utilizando
    ```bash
      docker stop $(docker ps -aq) && docker rm $(docker ps -aq)
   ```

3. Construa os containers com:
   ```bash
   docker-compose build --no-cache
   ```

4. Inicie os containers em segundo plano:
   ```bash
   docker-compose up -d
   ```

5. Verifique se os containers estão ativos:
   ```bash
   docker ps
   ```
-

A aplicação Flask foi feita com 15seg de atraso para subir após tudo inicializar, para que possa evitar de  ocorrer erro.


#Serviços Disponíveis
Após inicializar os containers, os seguintes serviços estarão disponíveis:

App Flask | [http://localhost:5001](http://localhost:5001) | #Devido a porta 5000 do meu Mac estar em uso pelo sistema, troquei para a 5001.
Grafana   | [http://localhost:3000](http://localhost:3000) |
MariaDB   | [http://localhost:3306]                        |
Prometheus| [http://localhost:9090](http://localhost:9090) |
-

#Configuração do Grafana
1. Acesse o Grafana: [http://localhost:3000](http://localhost:3000)
2. Faça login com as credenciais padrão:
   - Usuário: `admin`
   - Senha: `admin`

3. Navegue até a página inicial e explore o Dashboard, que exibirá os logs da aplicação Flask.

### Configuração de Data Source
1. Vá para: **Configuration > Data Sources**.
2. Data Sources Prometheus configurado.

---

#Utilizando a Aplicação Flask
1. Acesse a aplicação em: [http://localhost:5001](http://localhost:5001)
2. Clique em "Login" no canto superior direito.

3. Credenciais de login:
   - Usuário: `admin`
   - Senha: `admin`

# Cadastro de Alunos
# Método 1: Interface Web
1. Após o login, acesse: [http://localhost:5001/alunomodelview/list/](http://localhost:5001/alunomodelview/list/)

2. Utilize a interface para cadastrar novos alunos.

# Método 2: Postman
1. Crie uma requisição POST para: [http://localhost:5001/alunomodelview/](http://localhost:5001/alunomodelview/)
2. Use o seguinte corpo JSON:
   ```json
   {
       "nome": "Testar",
       "sobrenome": "TestarSobrenome",
       "turma": "Turma",
       "disciplinas": "Dc1, Dc2"
       "ra": "4321"
   }
   ``

3. Atualize a página para ver o novo aluno listado.


# Método 3: pytest
1. Dentro da Pasta "Flask" tem um arquivo "test_flask_app.py"
2. Este arquivo se trata de uma automação de Teste Py.
3. está automação realiza um teste de cadastro de usuário, dentro da pasta "Flask" -> "venv" tem o meu ambiente virtual, onde instalei todas as dependências da automação de teste.
3. Apos estar dentro da pasta "Flask" inicialize o ambiente virtual com o seguinte comando
   
    ```bash
    source venv/bin/activate
   ```
4. Apos estar com ambiente virtual ativo, utilize o comando "pytest" para inicializar o teste.
   ```bash
   pytest
   ```
5. Finalizado o teste, para sair do ambiente basta utilizar o comando.
   ```bash
   deactivate
   ```
-

#Pipeline de Automação com Jenkins
# Configuração do Jenkins
1. Inicie o Jenkins:
   ```bash
   sudo systemctl start jenkins
   sudo systemctl enable jenkins
   ```

2. Verifique o status do Jenkins:
   ```bash
   sudo systemctl status jenkins
   ```

3. Configure um pipeline utilizando o arquivo `Jenkinsfile` disponível no repositório.
4.  Acesse a aplicação em: [http://localhost:8080](http://localhost:8080)
5.  Faça login com as credenciais:
   - Usuário: `admin`
   - Senha: `4f2af4a5c77f499ab212b6d8ff4d2bb7`

# Fluxo do Pipeline
O pipeline automatiza a construção e o monitoramento da aplicação, garantindo integração contínua com o ambiente configurado.

---

#Arquitetura
O ambiente é composto pelas seguintes ferramentas e funcionalidades:
-Flask: API e interface para interação com alunos.
-Grafana: Monitoramento de métricas e logs.
-Prometheus: Coleta de métricas.
-MariaDB: Banco de dados para persistência.
-Jenkins: Automação de CI/CD.

---

#Referências
- Documentação oficial:
 -Docker - https://docs.docker.com/
 -Grafana - https://grafana.com/docs/
 -Prometheus - https://prometheus.io/docs/
 -Jenkins - https://www.jenkins.io/doc/
- Repositório: https://github.com/JeanGrendel/TrabalhoDevOps-RA-23.9730-5

-

Esse README foi estruturado para facilitar a leitura e o entendimento de quem for utilizar ou contribuir para o projeto.
