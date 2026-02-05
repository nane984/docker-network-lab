import pytest

pytestmark = pytest.mark.django_db

@pytest.mark.smoke
def test_app_is_alive(client):
    response = client.get("/health/")
    assert response.status_code == 200
