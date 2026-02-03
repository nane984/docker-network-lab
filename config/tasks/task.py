from celery import shared_task
import time
import logging

logger = logging.getLogger(__name__)

@shared_task(bind=True, autoretry_for=(Exception,), retry_backoff=5, retry_kwargs={'max_retries': 3})
def some_task(self):
    logger.info("Task started")
    time.sleep(15)
    logger.info("Task finished")
    return "Zadatak završen"