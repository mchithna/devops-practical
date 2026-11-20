from app import app


def test_index_returns_v2_message():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert response.data.decode() == "CI/CD and Docker Pipeline is a massive success! V2"
