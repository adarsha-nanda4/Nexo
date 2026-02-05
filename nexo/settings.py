import os
from pathlib import Path

# --------------------------------------------------
# Base
# --------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# --------------------------------------------------
# Environment handling
# --------------------------------------------------
# Load .env ONLY locally (Vercel ignores .env)
if os.getenv("VERCEL") is None:
    from dotenv import load_dotenv
    load_dotenv()

# --------------------------------------------------
# Security
# --------------------------------------------------
SECRET_KEY = 'django-insecure-)rbobb8i7()a3dr0j087_j3_**zbtel)1ga!@=&n^*-fagnh^p'

# DEBUG = os.getenv("DEBUG", "False") == "True"
DEBUG = True

ALLOWED_HOSTS = ["*"]

CSRF_TRUSTED_ORIGINS = [
    "https://*.vercel.app",
]

# --------------------------------------------------
# Applications
# --------------------------------------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Third-party
    "cloudinary",
    "cloudinary_storage",
    "pwa",

    # Local apps
    "Seller",
    "Product",
    "Route",
]

# --------------------------------------------------
# Middleware
# --------------------------------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# --------------------------------------------------
# URLs / WSGI
# --------------------------------------------------
ROOT_URLCONF = "nexo.urls"
WSGI_APPLICATION = "nexo.wsgi.application"

# --------------------------------------------------
# Templates
# --------------------------------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# --------------------------------------------------
# Database
# --------------------------------------------------
DB_ENGINE = os.getenv("DB_ENGINE", "neon")

if DB_ENGINE == "sqlite":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.getenv("NEON_DB_NAME"),
            "USER": os.getenv("NEON_DB_USER"),
            "PASSWORD": os.getenv("NEON_DB_PASSWORD"),
            "HOST": os.getenv("NEON_DB_HOST"),
            "PORT": os.getenv("NEON_DB_PORT", "5432"),
            "OPTIONS": {
                "sslmode": "require",
            },
        }
    }

# --------------------------------------------------
# Authentication
# --------------------------------------------------
AUTH_USER_MODEL = "Seller.Seller"

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# --------------------------------------------------
# Internationalization
# --------------------------------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# --------------------------------------------------
# Static & Media
# --------------------------------------------------
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STORAGES = {
    "default": {
        "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# --------------------------------------------------
# Cloudinary
# --------------------------------------------------
CLOUDINARY_URL = os.getenv("CLOUDINARY_URL")

if not CLOUDINARY_URL:
    raise RuntimeError("CLOUDINARY_URL is not set")

# --------------------------------------------------
# Default PK
# --------------------------------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# # --------------------------------------------------
# # PWA Settings
# # --------------------------------------------------
# PWA_APP_NAME = "Nexo"
# PWA_APP_DESCRIPTION = "Buy & Sell locally with Nexo"
# PWA_APP_THEME_COLOR = "#2563eb"
# PWA_APP_BACKGROUND_COLOR = "#ffffff"
# PWA_APP_DISPLAY = "standalone"
# PWA_APP_SCOPE = "/"
# PWA_APP_START_URL = "/"
# PWA_APP_ORIENTATION = "portrait"
# PWA_APP_STATUS_BAR_COLOR = "default"

# PWA_APP_ICONS = [
#     {
#         "src": "/static/icons/icon-192.png",
#         "sizes": "192x192",
#     },
#     {
#         "src": "/static/icons/icon-512.png",
#         "sizes": "512x512",
#     },
# ]

# PWA_APP_SPLASH_SCREEN = [
#     {
#         "src": "/static/icons/icon-512.png",
#         "media": "(device-width: 320px)",
#     }
# ]

# PWA_SERVICE_WORKER_PATH = os.path.join(
#     BASE_DIR, "static", "serviceworker.js"
# )
