# Basic configuration for running django

from pathlib import Path

# main project directory
BASE_DIR = Path(__file__).resolve().parent.parent

# secret key for django server
SECRET_KEY = 'django-insecure-)wljo9m0k!%u^q!500*lo4s@g*up26z9=$u9xa)jeejd-bzo@0'

# Debug mode for django project
# set DEBUG = False if in production mode
# set DEBUG = True if in debug mode
DEBUG = True

# Allows access to the website if the request is made from the following host url
ALLOWED_HOSTS = []

# installed django apps
# no app has been used in my project
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# lightweight plugin that processes during request and response execution
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# django urls
# django will go to collegerecommendation folder and search urls file when a url is entered
ROOT_URLCONF = 'collegerecommendation.urls'

# folder that contains tempaltes like HTML CSS
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['collegerecommendation/templates/'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'collegerecommendation.wsgi.application'


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

