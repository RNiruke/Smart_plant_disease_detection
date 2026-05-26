"""
Django Settings — Smart AI-Based Plant Disease Detection System
Development configuration (SQLite). Ready for MySQL in production.
"""

from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# ─────────────────────────────────────────────────────────────────────────────
# SECURITY
# ─────────────────────────────────────────────────────────────────────────────
SECRET_KEY = 'django-insecure-change-this-in-production-use-env-variable'
DEBUG = True
ALLOWED_HOSTS = ['*']


# ─────────────────────────────────────────────────────────────────────────────
# APPLICATIONS
# ─────────────────────────────────────────────────────────────────────────────
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third-party
    'crispy_forms',
    'crispy_bootstrap5',
    # Project apps
    'accounts',
    'detector',
    'advisory',
    'dashboard',
    'reports',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'plantdisease.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
            ],
        },
    },
]

WSGI_APPLICATION = 'plantdisease.wsgi.application'


# ─────────────────────────────────────────────────────────────────────────────
# CUSTOM USER MODEL
# ─────────────────────────────────────────────────────────────────────────────
AUTH_USER_MODEL = 'accounts.CustomUser'


# ─────────────────────────────────────────────────────────────────────────────
# DATABASE
# ─────────────────────────────────────────────────────────────────────────────
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# MySQL-compatible (uncomment for production):
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'plant_disease_db',
#         'USER': 'root',
#         'PASSWORD': 'yourpassword',
#         'HOST': 'localhost',
#         'PORT': '3306',
#     }
# }


# ─────────────────────────────────────────────────────────────────────────────
# AUTH SETTINGS
# ─────────────────────────────────────────────────────────────────────────────
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LOGIN_URL           = '/accounts/login/'
LOGIN_REDIRECT_URL  = '/dashboard/'
LOGOUT_REDIRECT_URL = '/'


# ─────────────────────────────────────────────────────────────────────────────
# INTERNATIONALISATION
# ─────────────────────────────────────────────────────────────────────────────
LANGUAGE_CODE = 'en'
TIME_ZONE     = 'Asia/Kolkata'
USE_I18N = True
USE_L10N = True
USE_TZ   = True

from django.utils.translation import gettext_lazy as _
LANGUAGES = [
    ('en', _('English')),
    ('hi', _('Hindi')),
    ('mr', _('Marathi')),
]
LOCALE_PATHS = [BASE_DIR / 'locale']


# ─────────────────────────────────────────────────────────────────────────────
# STATIC FILES
# ─────────────────────────────────────────────────────────────────────────────
STATIC_URL       = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT      = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# ─────────────────────────────────────────────────────────────────────────────
# MEDIA FILES  (user-uploaded images — profile pics, leaf photos)
# ─────────────────────────────────────────────────────────────────────────────
MEDIA_URL  = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# ─────────────────────────────────────────────────────────────────────────────
# CRISPY FORMS (Bootstrap 5)
# ─────────────────────────────────────────────────────────────────────────────
CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'
CRISPY_TEMPLATE_PACK          = 'bootstrap5'


# ─────────────────────────────────────────────────────────────────────────────
# FILE UPLOAD LIMITS
# (AI model settings will go here when you integrate your .pth model)
# ─────────────────────────────────────────────────────────────────────────────
MAX_UPLOAD_SIZE       = 10 * 1024 * 1024   # 10 MB
ALLOWED_IMAGE_TYPES   = ['image/jpeg', 'image/png', 'image/jpg', 'image/webp']

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
