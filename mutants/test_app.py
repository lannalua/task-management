import pytest
from app import app, tasks

@pytest.fixture
def client():
    with app.test_client() as client:
        # limpa a lista de tarefas antes de cada teste
        tasks.clear()
        yield client

BASE_URL = '/tasks'
tasks = []

def test_create_task(client):
    new_task_data = {
        "title": "Nova tarefa",
        "description": "Descrição da nova tarefa"
    }
    
    response = client.post(BASE_URL, json=new_task_data)
    assert response.status_code == 200
    response_json = response.get_json()
    assert "message" in response_json
    assert "id" in response_json
    tasks.append(response_json['id'])

def test_get_tasks(client):
    response = client.get(BASE_URL)
    assert response.status_code == 200
    response_json = response.get_json()
    assert "tasks" in response_json
    assert "total_tasks" in response_json

def test_get_task(client):
    if tasks:
        task_id = tasks[0]
        response = client.get(f"{BASE_URL}/{task_id}")
        assert response.status_code == 200
        response_json = response.get_json()
        assert task_id == response_json['id']

def test_update_task(client):
    if tasks:
        task_id = tasks[0]
        payload = {
            "completed": True,
            "description": "Nova descrição",
            "title": "Título atualizado"
        }
        response = client.put(f"{BASE_URL}/{task_id}", json=payload)
        assert response.status_code == 200
        response_json = response.get_json()
        assert "message" in response_json

        response = client.get(f"{BASE_URL}/{task_id}")
        assert response.status_code == 200
        response_json = response.get_json()
        assert response_json["title"] == payload["title"]
        assert response_json["description"] == payload["description"]
        assert response_json["completed"] == payload["completed"]

def test_delete_task(client):
    if tasks:
        task_id = tasks[0]
        response = client.delete(f"{BASE_URL}/{task_id}")
        assert response.status_code == 200

        response = client.get(f"{BASE_URL}/{task_id}")
        assert response.status_code == 404