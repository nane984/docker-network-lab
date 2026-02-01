from .base import *

# TEST baza (lokalno u Dockeru ili sqlite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',  # koristi in-memory DB za testove
    }
}

CELERY_TASK_ALWAYS_EAGER = True             # .delay() se izvršava odmah
CELERY_TASK_EAGER_PROPAGATES = True         # → exception ide direktno u test (vidiš grešku)

CELERY_BROKER_URL = "memory://"             # memory:// → nema Redis-a, nema network-a
CELERY_RESULT_BACKEND = "cache+memory://"