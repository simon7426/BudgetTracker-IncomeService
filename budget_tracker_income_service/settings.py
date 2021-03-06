from pathlib import Path
from datetime import timedelta
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DJANGO_DEBUG')

ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOST').split(' ')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'budget_tracker_income_service.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'budget_tracker_income_service.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {

        'ENGINE': os.environ.get('DJANGO_DB_ENGINE'),

        'NAME': os.environ.get('DJANGO_DB_NAME'),

        'USER': os.environ.get('DJANGO_DB_USER'),

        'PASSWORD': os.environ.get('DJANGO_DB_PASS'),

        'HOST': os.environ.get('DJANGO_DB_HOST'),

        'PORT': os.environ.get('DJANGO_DB_PORT'),

    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'rest_framework_simplejwt.authentication.JWTAuthentication',
#     ),
# }


# SIMPLE_JWT = {
#     'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
#     'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
#     'ROTATE_REFRESH_TOKENS': False,
#     'BLACKLIST_AFTER_ROTATION': False,
#     'UPDATE_LAST_LOGIN': False,

#     'ALGORITHM': 'HS256',
#     'SIGNING_KEY': SECRET_KEY,
#     'VERIFYING_KEY': None,
#     'AUDIENCE': None,
#     'ISSUER': None,

#     'AUTH_HEADER_TYPES': ('Bearer',),
#     'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
#     'USER_ID_FIELD': 'id',
#     'USER_ID_CLAIM': 'user_id',

#     'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
#     'TOKEN_TYPE_CLAIM': 'token_type',

#     'JTI_CLAIM': 'jti',

#     'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
#     'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
#     'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
# }

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGGING = {
   'version': 1,
   'disable_existing_loggers': True,
   'filters': {
       'filter_info_level': {
           '()': 'budget_tracker_income_service.log_middleware.FilterLevels',
           'filter_levels' : [
               "INFO"
           ]
       },
       'filter_error_level': {
           '()': 'budget_tracker_income_service.log_middleware.FilterLevels',
           'filter_levels' : [
               "ERROR"
           ]
       },
       'filter_warning_level': {
           '()': 'budget_tracker_income_service.log_middleware.FilterLevels',
           'filter_levels' : [
               "WARNING"
           ]
       }
   },
   'formatters': {
       'info-formatter': {
           'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
           'datefmt': '%Y-%m-%d %H:%M'
       },
       'error-formatter': {
           'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
           'datefmt': '%Y-%m-%d %H:%M'
       },
       'short': {
           'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
       }
   },
   'handlers': {
       'customHandler_1': {
           'formatter': 'info-formatter',
           'class': 'logging.StreamHandler',
           'filters': ['filter_info_level'],
       },
       'customHandler_2': {
           'formatter': 'error-formatter',
           'class': 'logging.StreamHandler',
           'filters': ['filter_error_level'],
       },
       'customHandler_3': {
           'formatter': 'short',
           'class': 'logging.StreamHandler',
           'filters': ['filter_warning_level'],
       },
   },
   'loggers': {
       'customLogger': {
           'handlers': [
               'customHandler_1',
               'customHandler_2',
               'customHandler_3'
           ],
           'level': 'DEBUG',
       },
   },
}
