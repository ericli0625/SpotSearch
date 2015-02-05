"""
Django settings for Eric project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
#BASE_DIR = /media/erichcli/Disk/Python-Project/Eric

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'vk2jtef6btb%zsfb!kqvlf9+@i2#d5$v8(b4&$82$8nh(lfnmd'

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
    'import_export',
    'spots',
    )

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'Eric.urls'

WSGI_APPLICATION = 'Eric.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

import dj_database_url
DATABASES = {'default': dj_database_url.config(default='postgres://qiivcofeurbrrq:ZrHRbAnPUaJTKo3lhyGCEKMMlI@ec2-54-83-204-104.compute-1.amazonaws.com:5432/d5sloc17vjd4sd')}


#DATABASES = {
#    'default': {
        #'ENGINE': 'django.db.backends.mysql',
#        'ENGINE': 'django.db.backends.sqlite3',   
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#        'NAME': 'travel_db',
#        'USER': 'root',                      
#        'PASSWORD': 'jmp275utn',                  
#        'HOST': '',                      
#        'PORT': '',                      
#    }
#}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = 'staticfiles' #????

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

# template -- web site
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "templates"),
)
