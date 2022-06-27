from .common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-7%sa5cjhet0apfn=rdk4m=d%a=pjizr$e_0q$q79ry@@1-cgr$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}