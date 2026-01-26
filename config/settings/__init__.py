import os
from ..celery import app as celery_app

ENV = os.environ.get("DJANGO_ENV", "dev")
__all__ = ("celery_app",)

if ENV == "prod":
    from .prod import *
else:
    from .dev import *
