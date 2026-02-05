import pytest
from core.models import Service

@pytest.mark.django_db
def test_multiple_services_saved():
    Service.objects.create(name="django")
    Service.objects.create(name="postgres")

    assert Service.objects.count() == 2