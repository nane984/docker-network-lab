import pytest
from core.models import Service

@pytest.mark.django_db
def test_service_creation():
    service = Service.objects.create(name="nginx")

    assert service.name == "nginx"
    assert service.is_active is True