
def test_create_user(client, db_session):
    response = client.post("/api/v1/users/", json={"name": "John Doe", "email": "john@example.com"})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "John Doe", "email": "john@example.com"}

def test_read_user(client, db_session):
    # Primero, crea un usuario
    client.post("/api/v1/users/", json={"name": "Jane Doe", "email": "jane@example.com"})
    response = client.get("/api/v1/users/1/")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Jane Doe", "email": "jane@example.com"}

def test_update_user(client, db_session):
    # Primero, crea un usuario
    client.post("/api/v1//users/", json={"name": "Alice", "email": "alice@example.com"})
    response = client.put("/api/v1/users/1/", json={"name": "Alice Smith", "email": "alice.smith@example.com"})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Alice Smith", "email": "alice.smith@example.com"}

def test_delete_user(client, db_session):
    # Primero, crea un usuario
    client.post("/api/v1/users/", json={"name": "Bob", "email": "bob@example.com"})
    response = client.delete("/api/v1/users/1/")
    assert response.status_code == 200
    response = client.get("/api/v1/users/1/")
    assert response.status_code == 404
