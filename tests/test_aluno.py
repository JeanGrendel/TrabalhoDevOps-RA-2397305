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
    response = client.post('/alunos', json={"nome": "Alex", "ra": "271823"})
    assert response.status_code == 201
