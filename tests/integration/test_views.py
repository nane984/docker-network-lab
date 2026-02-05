import pytest
from django.urls import reverse
from core.models import Service

@pytest.mark.django_db
def test_health_endpoint(client):
    Service.objects.create(name="redis")

    url = reverse("health")
    response = client.get(url)

    assert response.status_code == 200
    data = response.json()

    assert data["status"] == "ok"
    assert data["services"] == 1
