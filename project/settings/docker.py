from .base import *


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "drf_db",
        "USER": "user",
        "PASSWORD": "pass",
        "HOST": "db",
        "PORT": "5432",
    }
}
