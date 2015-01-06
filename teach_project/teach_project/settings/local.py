from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'teachoo_db',
        'USER':'davneet',
        'PASSWORD':'lol',
        'HOST':'localhost',
        'PORT':'',
    }
}
