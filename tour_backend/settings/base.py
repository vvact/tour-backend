import sys
from pathlib import Path

import logging
import logging.config
from django.utils.log import DEFAULT_LOGGING

import environ
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# Correct: three parents to go from settings/base.py to project root
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# --- ADD THIS BLOCK: Add 'apps' directory to Python's import path ---
sys.path.insert(0, str(BASE_DIR / "apps"))
# ----------------------------------------------------------------

# Load .env from the project root – works on any machine
env_file = BASE_DIR / ".env"
if not env_file.exists():
    raise FileNotFoundError(
        f"❌ .env file not found at {env_file}. " "Please create one using .env.example as a template."
    )
load_dotenv(env_file, override=True)

# Initialize environ (reads from os.environ, which load_dotenv just populated)
env = environ.Env(DEBUG=(bool, False), ALLOWED_HOSTS=(list, []))

# Now read the variables – they come from the environment
SECRET_KEY = env("SECRET_KEY")
DEBUG = env("DEBUG")
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")


# Application definition

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "whitenoise.runserver_nostatic",
    "django.contrib.staticfiles",
    "django.contrib.sites",
]

THIRF_PARTY_APPS = [
    "rest_framework",
    "corsheaders",
    "django_filters",
    "drf_spectacular",
]

LOCAL_APPS = [
    "core",
    "users",
]

INSTALLED_APPS = DJANGO_APPS + THIRF_PARTY_APPS + LOCAL_APPS
SITE_ID = 1

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "tour_backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "tour_backend.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {"default": env.db("DATABASE_URL", default="sqlite:///db.sqlite3")}

# Ensure the database connection uses the correct engine
DATABASES["default"]["ATOMIC_REQUESTS"] = True

# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


AUTH_USER_MODEL = 'users.User'

# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Africa/Nairobi"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

# Static files (CSS, JavaScript, Images)
STATIC_URL = "/static/"  # <-- Missing leading slash; let's fix
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
STATIC_ROOT = BASE_DIR / "staticfiles"

# Media files (User-uploaded files)
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Phone number field configuration
PHONENUMBER_DEFAULT_REGION = "KE"

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    ],
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend",
    ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_THROTTLE_CLASSES": [
        "rest_framework.throttling.AnonRateThrottle",
        "rest_framework.throttling.UserRateThrottle",
    ],
    "DEFAULT_THROTTLE_RATES": {
        "anon": "100/day",
        "user": "1000/day",
    },
    "EXCEPTION_HANDLER": "core.exceptions.custom_exception_handler",
}

SPECTACULAR_SETTINGS = {
    "TITLE": "Tour Backend API",
    "DESCRIPTION": "API for managing tours, bookings, and reviews",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
}



# ============================================
# LOGGING CONFIGURATION
# ============================================
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,  # Preserve Django's default loggers

    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
        'django': {
            'format': '{levelname} {asctime} {name} {message}',
            'style': '{',
        },
    },

    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
            'level': 'DEBUG',   # Console always shows debug in dev
        },
        'file_general': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': BASE_DIR / 'logs' / 'django.log',
            'maxBytes': 1024 * 1024 * 10,  # 10 MB
            'backupCount': 5,
            'formatter': 'verbose',
            'level': 'INFO',
        },
        'file_errors': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': BASE_DIR / 'logs' / 'errors.log',
            'maxBytes': 1024 * 1024 * 10,
            'backupCount': 5,
            'formatter': 'verbose',
            'level': 'ERROR',
        },
    },

    'loggers': {
        # Django core loggers
        'django': {
            'handlers': ['console', 'file_general', 'file_errors'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.request': {
            'handlers': ['console', 'file_errors'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'WARNING',   # Set to DEBUG to see SQL queries
            'propagate': False,
        },
        # Third‑party app loggers
        'rest_framework': {
            'handlers': ['console', 'file_general'],
            'level': 'INFO',
            'propagate': False,
        },
        # Your custom apps
        'core': {
            'handlers': ['console', 'file_general'],
            'level': 'DEBUG',      # Will be overridden in prod
            'propagate': False,
        },
        'core': {
            'handlers': ['console', 'file_general'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },

    # Root logger – captures everything not covered above
    'root': {
        'handlers': ['console', 'file_general', 'file_errors'],
        'level': 'INFO',
    },
}