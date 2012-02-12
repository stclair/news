# Development settings for news
from settings.defaults import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Change this to work with your default development database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'USER': 'mad',                       # Not used with sqlite3.
        'PASSWORD': 'winterset',                   # Not used with sqlite3.
        'HOST': '127.0.0.1',                       # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                       # Set to empty string for default. Not used with sqlite3.
        'NAME': 'madisonian',
    }
}

# URL configuration to use in development mode
ROOT_URLCONF = 'urls.development'


# Attempt to load any settings from settings.local_development, but ignore any
# errors complaining about them not being present.
try:
    from settings.local_development import *
except ImportError, e:
    pass
