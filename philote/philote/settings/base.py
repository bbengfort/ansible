# philote.settings.base
# Base Django settings for philote project.
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Sat Apr 12 11:24:32 2014 -0400
#
# Copyright (C) 2014 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: base.py [] benjamin@bengfort.com $

"""
Django settings for philote project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

##########################################################################
## Imports
##########################################################################

import os

##########################################################################
## Helper function for environmental settings
##########################################################################

def environ_setting(name, default=None):
    """
    Fetch setting from the environment- if not found, then this setting is
    ImproperlyConfigured.
    """
    if name not in os.environ and default is None:
        from django.core.exceptions import ImproperlyConfigured
        raise ImproperlyConfigured(
            "The {0} ENVVAR is not set.".format(name)
        )

    return os.environ.get(name, default)

##########################################################################
## Build Paths inside of project with os.path.join
##########################################################################

BASE_DIR    = os.path.dirname(os.path.dirname(__file__))
PROJECT_DIR = os.path.normpath(os.path.join(BASE_DIR, os.pardir))
ANSIBLE_DIR = os.path.normpath(os.path.join(PROJECT_DIR, os.pardir))

##########################################################################
## Secret settings - do not store!
##########################################################################

SECRET_KEY = environ_setting("SECRET_KEY", "")

##########################################################################
## Database Settings
##########################################################################

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(ANSIBLE_DIR, 'fixtures/philote.db'),
    }
}

##########################################################################
## Runtime settings
##########################################################################

## Debugging Settings
DEBUG            = False
TEMPLATE_DEBUG   = False

## Hosts
ALLOWED_HOSTS    = []

## WSGI Configuration
ROOT_URLCONF     = 'philote.urls'
WSGI_APPLICATION = 'philote.wsgi.application'

## Application Definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'flowr',
)

## Request Handling
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

## Localization
LANGUAGE_CODE = 'en-us'
TIME_ZONE     = 'America/New_York'
USE_I18N      = True
USE_L10N      = True
USE_TZ        = True

##########################################################################
## Content (Static, Media, Templates)
##########################################################################

## Static Files
STATIC_URL          =  '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

STATICFILES_DIRS    = (
    os.path.join(PROJECT_DIR, 'static'),
)

## Template Files.
TEMPLATE_DIRS       = (
    os.path.join(PROJECT_DIR, 'templates'),
)

## Uploaded Media
MEDIA_URL           = "/media/"

##########################################################################
## Logging and Error Reporting
##########################################################################

ADMINS          = (
    ('Benjamin Bengfort', 'benjamin@bengfort.com'),
)

SERVER_EMAIL    = 'Dakota <server@bengfort.com>'
EMAIL_USE_TLS   = True
EMAIL_HOST      = 'smtp.gmail.com'
EMAIL_HOST_USER = 'server@bengfort.com'
EMAIL_HOST_PASSWORD = environ_setting("EMAIL_HOST_PASSWORD", "")
EMAIL_PORT      = 587

##########################################################################
## Ansible Settings
##########################################################################

ANSIBLE_HOST = 'localhost'
ANSIBLE_PORT = 1025
ANSIBLE_TIMEOUT = 10
