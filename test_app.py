import pytest
from app import app, tasks

@pytest.fixture
def client():
    with app.test_client() as client:
        # limpa a lista de tarefas antes de cada teste
        tasks.clear()
        yield client

def test_create_task(client):
    response = client.post("/tasks", json={"title": "Nova tarefa", "description": "Teste"})
    assert response.status_code == 200
    json_data = response.get_json()
    assert "id" in json_data
    assert json_data["message"] == "Nova tarefa criada com sucesso"

def test_get_tasks(client):
    client.post("/tasks", json={"title": "Tarefa 1"})
    response = client.get("/tasks")
    assert response.status_code == 200
    json_data = response.get_json()
    assert "tasks" in json_data
    assert json_data["total_tasks"] == 1

def test_update_task(client):
    r = client.post("/tasks", json={"title": "Teste", "description": "desc"})
    task_id = r.get_json()["id"]

    payload = {"title": "Atualizado", "description": "Nova desc", "completed": True}
    response = client.put(f"/tasks/{task_id}", json=payload)
    assert response.status_code == 200

    r2 = client.get(f"/tasks/{task_id}")
    task = r2.get_json()
    assert task["title"] == payload["title"]
    assert task["completed"] == payload["completed"]

def test_delete_task(client):
    r = client.post("/tasks", json={"title": "Teste"})
    task_id = r.get_json()["id"]

    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 200

    r2 = client.get(f"/tasks/{task_id}")
    assert r2.status_code == 404
