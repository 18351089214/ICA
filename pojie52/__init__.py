import os

from django.apps import AppConfig

default_app_config = 'pojie52.Pojie52Config'


def get_current_app_name(_file):
    return os.path.split(os.path.dirname(_file))[-1]


class Pojie52Config(AppConfig):
    name = get_current_app_name(__file__)
    verbose_name = '吾爱破解'
