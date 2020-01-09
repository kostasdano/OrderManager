from .base import *
import dj_database_url
from dj_config_url import config
DEBUG = False

ALLOWED_HOSTS = ['kostasdano-ordermanager.herokuapp.com',]


DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}