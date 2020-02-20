import os

from django.apps import AppConfig

default_app_config = 'qqshare.QQShareConfig'


def get_current_app_name(_file):
    return os.path.split(os.path.dirname(_file))[-1]


class QQShareConfig(AppConfig):
    name = get_current_app_name(__file__)
    verbose_name = 'QQ群共享文件'
