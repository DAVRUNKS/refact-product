def test_register_user(client):

    response = client.post(
        "/register",
        json={
            "username": "apiuser",
            "password": "password123"
        }
    )

    assert response.status_code == 201

    data = response.get_json()

    assert data["message"] == "User registered successfully"
    
def test_register_without_username(client):

    response = client.post(
        "/register",
        json={
            "password": "password123"
        }
    )

    assert response.status_code == 400

    data = response.get_json()

    assert data["error"] == "Username is required"
    
def test_register_with_short_password(client):

    response = client.post(
        "/register",
        json={
            "username": "shortuser",
            "password": "123"
        }
    )

    assert response.status_code == 400

    data = response.get_json()

    assert data["error"] == "Password must be at least 6 characters"
    
def test_register_duplicate_user(client):

    client.post(
        "/register",
        json={
            "username": "duplicateuser",
            "password": "password123"
        }
    )

    response = client.post(
        "/register",
        json={
            "username": "duplicateuser",
            "password": "password456"
        }
    )

    assert response.status_code == 409

    data = response.get_json()

    assert data["error"] == "Username already exists"
    
def test_get_product_by_id(client):

    response = client.post(
        "/products",
        json={
            "name": "Laptop",
            "price": 1500
        },
        headers={
            "Authorization": "Bearer testtoken"
        }
    )

    assert response.status_code == 201

    product_id = response.get_json()["id"]

    response = client.get(
        f"/products/{product_id}"
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["id"] == product_id
    assert data["name"] == "Laptop"
    assert data["price"] == 1500
    
def test_get_product_not_found(client):

    response = client.get(
        "/products/99999"
    )

    assert response.status_code == 404

    data = response.get_json()

    assert data["error"] == "Product not found"

def test_update_product(client):

    response = client.post(
        "/products",
        json={
            "name": "Laptop",
            "price": 1500
        },
        headers={
            "Authorization": "Bearer testtoken"
        }
    )

    assert response.status_code == 201

    product_id = response.get_json()["id"]

    response = client.put(
        f"/products/{product_id}",
        json={
            "name": "Gaming Laptop",
            "price": 2000
        },
        headers={
            "Authorization": "Bearer testtoken"
        }
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["id"] == product_id
    assert data["name"] == "Gaming Laptop"
    assert data["price"] == 2000
    
def test_delete_product(client):

    response = client.post(
        "/products",
        json={
            "name": "Laptop",
            "price": 1500
        },
        headers={
            "Authorization": "Bearer testtoken"
        }
    )

    assert response.status_code == 201

    product_id = response.get_json()["id"]

    response = client.delete(
        f"/products/{product_id}",
        headers={
            "Authorization": "Bearer testtoken"
        }
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["message"] == "Product deleted successfully"
    
def test_delete_product_not_found(client):

    response = client.delete(
        "/products/99999",
        headers={
            "Authorization": "Bearer testtoken"
        }
    )

    assert response.status_code == 404

    data = response.get_json()

    assert data["error"] == "Product not found"