# tour_backend/settings/dev.py
from .base import *


# Override with development-specific values
DEBUG = env('DEBUG')  # Should be True in .env
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')  # e.g., localhost,127.0.0.1

# Use SQLite (or your preferred local DB)
DATABASES = {
    'default': env.db('DATABASE_URL', default='sqlite:///db.sqlite3')
}

# Additional dev-only apps (optional, e.g., django-debug-toolbar)
# INSTALLED_APPS += ['debug_toolbar']

# Dev-only middleware
# MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']