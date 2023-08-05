# -*- coding: utf-8 -*-
from __future__ import unicode_literals

SECRET_KEY = 'iz@*(xuwo+a2a2r+jb1p8-ap8hic1_l(h$vj(mr_v!d6%ijr1n'

DEBUG = True

TEMPLATE_DEBUG = True


ALLOWED_HOSTS = []

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #     'django.template.loaders.eggs.Loader',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
            ],
        },
    },
]

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_reamaze',)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

STATIC_URL = '/static/'


REAMAZE_SECRET_KEY = b"125acdef1425da15af6cd8870a878c878c48cc8"
REAMAZE_JS_URL = "//URL/reamaze.js"
REAMAZE_ACCOUNT = "ACCOUNT_NAME"
REAMAZE_CHANNEL = "CHANNEL_NAME"
REAMAZE_OK_FOR_ANONYMOUS = True
REAMAZE_PREFIX_USER_ID = None
