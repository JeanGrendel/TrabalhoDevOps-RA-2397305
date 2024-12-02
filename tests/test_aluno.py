import pytest
from flask import Flask
from app import app, db, Aluno

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_adicionar_aluno(client):
    response = client.post('/alunos', json={
        "nome": "Alex",
        "sobrenome": "Oliveira",
        "turma": "4F",
        "disciplinas": "Devops, Java"
    })
    assert response.status_code == 201
    assert b"Aluno adicionado com sucesso!" in response.data

def test_listar_alunos(client):
    response = client.get('/alunos')
    assert response.status_code == 200
    alunos = response.get_json()
    assert len(alunos) > 0
