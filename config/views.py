from .tasks.task import some_task
from django.http import HttpResponse

import logging

logger = logging.getLogger(__name__)


def test_view(request):
    logger.info("Ovo je info log")
    logger.warning("Ovo je warning")
    logger.error("Ovo je error")
    some_task.delay()
    return HttpResponse("Task poslat u background")

def test_view2(request):
    a  = 1/0
    return HttpResponse("view 2 koji je pod greskom")