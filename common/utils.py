# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
from common.consts import PATH_TO_UI, PATH_TO_USER_DATA, PATH_TO_PROGRAM_DATA


def path_to_ui(path):
    return f'{PATH_TO_UI}/{path}.ui'


def path_to_user_data(path):
    return f'{PATH_TO_USER_DATA}/{path}'


def path_to_program_data(path):
    return f'{PATH_TO_PROGRAM_DATA}/{path}'


def format_time(time):
    s = time % 60
    m = time // 60 % 60
    h = time // 3600
    return f'{h // 10}{h % 10}:{m // 10}{m % 10}:{s // 10}{s % 10}'
