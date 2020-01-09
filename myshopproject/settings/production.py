from .base import *

DEBUG = False

ALLOWED_HOSTS = ['kostasdano-ordermanager.herokuapp.com',]


DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}