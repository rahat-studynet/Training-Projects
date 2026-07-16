"""
Django settings for agent_system project.

This file contains the main project configuration:
- Installed apps
- Database setup
- Template configuration
- Authentication redirects
- DRF API configuration
- Static and media file configuration
"""

import os
from pathlib import Path


# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent


# Secret key for local development
SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    "django-insecure-change-this-key-for-local-development-only"
)


# Development mode
DEBUG = True


# Allowed hosts for local development
ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
]


# Installed apps of this project
INSTALLED_APPS = [
    # Django default apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Third-party apps
    "rest_framework",
    "rest_framework.authtoken",

    # Local apps
    "accounts",
    "cart",
]


# Django REST Framework configuration
REST_FRAMEWORK = {
    # Authentication methods for API
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ],

    # Default API permission
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],

    # Custom API error response
    "EXCEPTION_HANDLER": "cart.exceptions.custom_api_exception_handler",
}


# Middleware works between request and response
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# Main URL configuration file
ROOT_URLCONF = "agent_system.urls"


# Template configuration
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",

        # We will keep templates inside each app
        "DIRS": [],

        # This allows Django to find templates inside app/templates/
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


# WSGI application
WSGI_APPLICATION = "agent_system.wsgi.application"


# Database configuration
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation rules
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Login and logout redirects
LOGIN_URL = "/signin/"
LOGIN_REDIRECT_URL = "/products/"
LOGOUT_REDIRECT_URL = "/"


# Media file configuration for product images
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"


# Language and time zone
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


# Static file configuration
STATIC_URL = "/static/"


# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"