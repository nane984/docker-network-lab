from django.http import JsonResponse
from .models import Service

def health_check(request):
    return JsonResponse({
        "status": "ok",
        "services": Service.objects.count()
    })