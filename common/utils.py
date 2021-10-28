# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
from common.consts import PATH_TO_UI, PATH_TO_USER_DATA


def path_to_ui(path):
    return f'{PATH_TO_UI}/{path}.ui'


def path_to_user_data(path):
    return f'{PATH_TO_USER_DATA}/{path}'
