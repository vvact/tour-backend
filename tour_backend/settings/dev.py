# tour_backend/settings/dev.py
from .base import *

# ============================================
# DEVELOPMENT-SPECIFIC SETTINGS
# ============================================

# Debug & Hosts
DEBUG = env('DEBUG')                        # Should be True in .env
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')   # localhost,127.0.0.1

# Database (SQLite for development)
DATABASES = {
    'default': env.db('DATABASE_URL', default='sqlite:///db.sqlite3')
}

# ============================================
# STATIC & MEDIA FILES (Served in development)
# ============================================
# NOTE: Static and media files are automatically served by Django's
#       runserver when DEBUG=True. The URL patterns are added in
#       tour_backend/urls.py (see the `if settings.DEBUG:` block).
#       No extra settings are needed here; everything is inherited
#       from base.py (STATIC_URL, MEDIA_URL, STATIC_ROOT, MEDIA_ROOT).

# ============================================
# OPTIONAL: Development-only apps
# ============================================
# Uncomment to add django-debug-toolbar:
# INSTALLED_APPS += ['debug_toolbar']
# MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']