# tour_backend/settings/__init__.py
from .base import env

# Read the environment type from .env (defaults to 'dev')
ENVIRONMENT = env("ENVIRONMENT", default="dev")

if ENVIRONMENT == "production":
    from .production import *
else:
    from .dev import *
