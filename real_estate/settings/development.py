from .base import *

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DEFAULT_FROM_EMAIL = "info@real-estate.com"
EMAIL_BACKEND = 'djcelery_email.backends.CeleryEmailBackend'

DATABASES = {
    "default": {
        "ENGINE": env("POSTGRES_ENGINE"),
        "NAME": env("POSTGRES_DB"),
        "USER": env("POSTGRES_USER"),
        "PASSWORD": env("POSTGRES_PASSWORD"),
        "HOST": env("PG_HOST"),
        "PORT": env("PG_PORT"),
    }
}

CELERY_BROKER_URL = env('CELERY_BROKER')
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True
RESULT_BACKEND = env('CELERY_BACKEND')
TIMEZONE = 'America/Phoenix'