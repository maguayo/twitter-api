"""Development settings."""

from .base import *  # NOQA
from .base import env

# Base
DEBUG = True

# NEVER write the key here, this is just an example
SECRET_KEY = "89)&58beji*g#))=_rnuj%&dr%sry_0yn&j6nlly#fuugq1&2d"

ALLOWED_HOSTS = ["*"]

# Templates
TEMPLATES[0]["OPTIONS"]["debug"] = DEBUG  # NOQA

LOGGING = {
    'version': 1,
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'DEBUG',
            'handlers': ['console'],
        }
    }
}