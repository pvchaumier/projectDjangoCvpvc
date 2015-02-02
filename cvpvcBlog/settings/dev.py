import os
from cvpvcBlog.settings.base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True
# DEBUG = False
# TEMPLATE_DEBUG = False


INSTALLED_APPS += (
    'django_extensions',
#    'debug_toolbar',
)

MIDDLEWARE_CLASSES += (
#    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'NAME': 'dbcvpvc',
#        'USER': 'dbadmin',
#        'PASSWORD': 'dbadminmdp',
#    }
# }
