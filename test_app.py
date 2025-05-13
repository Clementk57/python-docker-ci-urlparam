import pytest
from app import app as flask_app

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_root_path(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'<h1>Bienvenue !</h1>' in response.data
    assert b'/hello/VOTRE_NOM' in response.data

def test_hello_with_name_parameter(client):
    test_name = "DockerCI"
    response = client.get(f'/hello/{test_name}')
    assert response.status_code == 200
    assert f'<h1>Hello, {test_name}!</h1>'.encode() in response.data

def test_hello_with_another_name(client):
    test_name = "Utilisateur"
    response = client.get(f'/hello/{test_name}')
    assert response.status_code == 200
    assert f'<h1>Hello, {test_name}!</h1>'.encode() in response.data
