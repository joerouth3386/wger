import os
import environ
from datetime import timedelta
from wger.settings_global import *

# Setup environment variables
env = environ.Env(
    DJANGO_DEBUG=(bool, False)
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Core Django settings
DEBUG = env.bool("DJANGO_DEBUG", default=False)

SECRET_KEY = env.str("SECRET_KEY", "CHANGE-ME-TO-A-SECRET-STRING")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=['localhost', '127.0.0.1', 'www.uncagedgrowth.online'])

STATIC_URL = env.str('STATIC_URL', '/static/')
STATIC_ROOT = env.str("DJANGO_STATIC_ROOT", os.path.join(BASE_DIR, 'staticfiles'))

MEDIA_URL = env.str('MEDIA_URL', '/media/')
MEDIA_ROOT = env.str("DJANGO_MEDIA_ROOT", os.path.join(BASE_DIR, 'media'))

CSRF_TRUSTED_ORIGINS = env.list(
    "CSRF_TRUSTED_ORIGINS",
    default=['https://www.uncagedgrowth.online']
)
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# Database (PostgreSQL for production)
DATABASES = {
    'default': {
        'ENGINE': env.str("DJANGO_DB_ENGINE", "django.db.backends.postgresql"),
        'NAME': env.str("DJANGO_DB_DATABASE"),
        'USER': env.str("DJANGO_DB_USER"),
        'PASSWORD': env.str("DJANGO_DB_PASSWORD"),
        'HOST': env.str("DJANGO_DB_HOST"),
        'PORT': env.str("DJANGO_DB_PORT", "5432"),
    }
}

# Email configuration
EMAIL_BACKEND = env.str('EMAIL_BACKEND', 'django.core.mail.backends.smtp.EmailBackend')
EMAIL_HOST = env.str("EMAIL_HOST", "smtp.gmail.com")
EMAIL_PORT = env.int("EMAIL_PORT", 587)
EMAIL_HOST_USER = env.str("EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = env.str("EMAIL_HOST_PASSWORD", "")
EMAIL_USE_TLS = env.bool("EMAIL_USE_TLS", True)
EMAIL_USE_SSL = env.bool("EMAIL_USE_SSL", False)
DEFAULT_FROM_EMAIL = env.str("FROM_EMAIL", "wger Workout Manager <wger@example.com>")

# Celery (optional)
CELERY_BROKER_URL = env.str("CELERY_BROKER", "redis://localhost:6379/2")
CELERY_RESULT_BACKEND = env.str("CELERY_BACKEND", "redis://localhost:6379/2")

# Auth Proxy (SSO/Reverse Proxy)
AUTH_PROXY_HEADER = env.str("AUTH_PROXY_HEADER", "")
AUTH_PROXY_TRUSTED_IPS = env.list("AUTH_PROXY_TRUSTED_IPS", default=[])
AUTH_PROXY_CREATE_UNKNOWN_USER = env.bool("AUTH_PROXY_CREATE_UNKNOWN_USER", False)
AUTH_PROXY_USER_EMAIL_HEADER = env.str("AUTH_PROXY_USER_EMAIL_HEADER", "")
AUTH_PROXY_USER_NAME_HEADER = env.str("AUTH_PROXY_USER_NAME_HEADER", "")

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': env.str('LOG_LEVEL_PYTHON', 'INFO').upper(),
    },
}

# Timezone
TIME_ZONE = env.str("TIME_ZONE", "Europe/Berlin")

# Site URL
SITE_URL = env.str('SITE_URL', 'https://www.uncagedgrowth.online')

# Optionals: Uncomment and configure if needed
# WGER_SETTINGS = {}

# Django Axes, DRF, SimpleJWT, etc. can be configured as needed here, but ensure variables are defined before use.

# If using forwarded protocol headers (e.g., behind a proxy/load balancer)
if env.bool('X_FORWARDED_PROTO_HEADER_SET', False):
    SECURE_PROXY_SSL_HEADER = (
        env.str('SECURE_PROXY_SSL_HEADER', 'HTTP_X_FORWARDED_PROTO'),
        'https'
    )

# Static and media file locations
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')] if os.path.exists(os.path.join(BASE_DIR, 'static')) else []

# Optional: add REST_FRAMEWORK or other advanced settings here as needed
