"""
Django settings for shopSmart project.

Generated by 'django-admin startproject' using Django 2.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import os.path

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'vy-&@g(%e=ts+49fkxs*mb6)&kzu@u7gq6jb=9hs&cx*rc_w3w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

LOGIN_URL = 'login'
# Application definition

INSTALLED_APPS = [
#loacal apps
    'shopSmart',
    'django_crontab',
   # 'shopSmart.apps.SuitConfig',
    'account',
    'django.contrib.admin',
    'admin_interface',
    'colorfield',
    'django.contrib.postgres',
    'django_celery_results',
    'django_celery_beat',
    'django_filters',
    'bootstrapform',
    'social_django',
    #'whoosh',
    #'haystack',
    
#biult in apps
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
#local middleware
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'shopSmart.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'social_django.context_processors.login_redirect',
                'social_django.context_processors.backends',
            ],
        },
    },
]

WSGI_APPLICATION = 'shopSmart.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'shopsmart_db',
#         'USER': 'raheel',
#         'PASSWORD': '123',
#         'HOST': 'localhost',
#         'PORT': '3306',
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ssdb',
        'USER': 'postgres',
        'PASSWORD': 'Xherry786',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
AUTHENTICATION_BACKENDS = (
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.github.GithubOAuth2',

    'django.contrib.auth.backends.ModelBackend',
)
# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators
USER_AUTH_MODEL = 'account.Account'
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = ''
# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# WHOOSH_INDEX = os.path.join('', '/whoosh/')
# HAYSTACK_CONNECTIONS = {
#     "default":{
#         'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
#         'PATH': WHOOSH_INDEX,
#     },
# }
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = ''
STATICFILES_DIRS = ( os.path.join('static'), )

# setting up celery
AUTH_USER_MODEL = 'account.Account'
AUTH_PROFILE_MODULE = 'account.AccountProfile'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
CELERY_RESULT_BACKEND = 'django-db'
CELERY_CACHE_BACKEND = 'django-cache'


#SMTP configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'noreplyshopsmart@gmail.com'
EMAIL_HOST_PASSWORD = 'viqqfcjusjfjfmwc'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'ShopSmart Admin <noreply@shopsmart.com>'

# setting up all auth
SITE_ID = 1


#define cron jobs
CRONJOBS = [
    ('* */12 * * *','account.cron.updation') #shedules for every 12th hr
]