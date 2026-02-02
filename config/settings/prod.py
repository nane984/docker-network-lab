from .base import *
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.celery import CeleryIntegration

sentry_sdk.init(
    dsn=os.getenv("SENTRY_DSN"),
    integrations=[
        DjangoIntegration(),
        CeleryIntegration(),
    ],
    traces_sample_rate=0.1,
    send_default_pii=False,
)

DEBUG = False

# Hostovi koji smeju da pristupe
ALLOWED_HOSTS = ["mydomen.com", "localhost"]     #obavezno localhost obrisati za production

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# SSL i HTTPS
SECURE_SSL_REDIRECT = True                      # redirect HTTP -> HTTPS
SESSION_COOKIE_SECURE = True                    # cookie samo preko HTTPS
CSRF_COOKIE_SECURE = True                       # CSRF cookie samo preko HTTPS

SECURE_REDIRECT_EXEMPT = [r"^health/$"]         # da bi vracao health obicno, ne preko https

# HSTS (HTTP Strict Transport Security)
SECURE_HSTS_SECONDS = 31536000 # 1 godina
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# XSS i Content Security
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True


# Clickjacking
X_FRAME_OPTIONS = "DENY"


# CSRF
CSRF_TRUSTED_ORIGINS = ["https://mydomain.com", "localhost"]        #obavezno localhost obrisati za production

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOWED_ORIGINS = [
    "https://mydomain.com",
    "localhost",                                                    # za produkciju obavezno obrisati localhost
]
