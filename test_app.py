from app import app


def test_index_returns_v1_message():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert response.data.decode() == "Hello, DevOps World! V1"
