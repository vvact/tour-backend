# tour_backend/settings/production.py
import sentry_sdk

from .base import *  # noqa: F401, F403
from .base import env

# Force DEBUG off in production (never rely on .env for this in prod, but we'll enforce it)
DEBUG = False

# Read ALLOWED_HOSTS from .env (e.g., yourdomain.com,www.yourdomain.com)
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

# Use a production database (e.g., PostgreSQL)
# Ensure DATABASE_URL in .env points to your production DB
DATABASES = {"default": env.db("DATABASE_URL")}


# sentry
sentry_sdk.init(dsn=env("SENTRY_DSN", default=""))

# --- Security Settings (Critical for Production) ---
# Redirect all HTTP traffic to HTTPS
SECURE_SSL_REDIRECT = True

# Cookies only sent over HTTPS
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Protect against XSS and clickjacking
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"

# HSTS (HTTP Strict Transport Security) - uncomment when your SSL cert is ready
# SECURE_HSTS_SECONDS = 31536000  # 1 year
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_PRELOAD = True

# Use a secure proxy header (if behind Nginx/Apache)
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Static & Media file serving (in production, use WhiteNoise or separate CDN)
# We'll add Whitenoise later, but for now, make sure STATIC_ROOT is set
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
