"""
Django settings for car_tracking project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'm_0u@^nw+b#!=a$)cz565g8riyutr__wk)88tudj$)-ogn-%e#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_openid_auth',
    'mainapp',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'car_tracking.urls'

WSGI_APPLICATION = 'car_tracking.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT =  os.path.join(BASE_DIR,'public')
STATICFILES_DIRS = (
    ("js", os.path.join(BASE_DIR, "assets/js")),
    ("js", os.path.join(BASE_DIR, "assets/bootstrap/js")),
    ("css", os.path.join(BASE_DIR, "assets/css")),
    ("css", os.path.join(BASE_DIR, "assets/bootstrap/css")),
    ("img", os.path.join(BASE_DIR, "assets/imgs")),
)
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "templates"),
)
##################################################


SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

AUTHENTICATION_BACKENDS = (
    'django_openid_auth.auth.OpenIDBackend',
    'django.contrib.auth.backends.ModelBackend',
)

# Should users be created when new OpenIDs are used to log in?
OPENID_CREATE_USERS = True

# When logging in again, should we overwrite user details based on
# data received via Simple Registration?
OPENID_UPDATE_DETAILS_FROM_SREG = True

# If set, always use this as the identity URL rather than asking the
# user.  This only makes sense if it is a server URL.
OPENID_SSO_SERVER_URL = 'https://www.google.com/accounts/o8/id'

# Tell django.contrib.auth to use the OpenID signin URLs.
LOGIN_URL = '/openid/login/'
LOGIN_REDIRECT_URL = '/'

# Should django_auth_openid be used to sign into the admin interface?
OPENID_USE_AS_ADMIN_LOGIN = False

GOOGLE_MAPS_V3_API_KEY = 'AIzaSyBMJ7nWrYa4f9llXp6rMqUBfTFcn4kEjg8'