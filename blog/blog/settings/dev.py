from __future__ import absolute_import, unicode_literals

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'yo=s^8^bq*46b$)6sc!g&jhdv9q(p6fu35bwic#()&+-f6*)@&'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
