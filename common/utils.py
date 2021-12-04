# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
import csv

from pymorphy2 import MorphAnalyzer

from common.consts import PATH_TO_UI, PATH_TO_USER_DATA, PATH_TO_PROGRAM_DATA, BASE_BOARD_CELLS


def path_to_ui(path):
    return f'{PATH_TO_UI}/{path}.ui'


def path_to_user_data(path):
    return f'{PATH_TO_USER_DATA}/{path}'


def path_to_program_data(path):
    return f'{PATH_TO_PROGRAM_DATA}/{path}'


def format_moves_count(moves_count):
    morph_analyzer = MorphAnalyzer(path='pm_data/')
    move_word = morph_analyzer.parse('ход')[0].\
        make_agree_with_number(moves_count).word
    return f'{moves_count} {move_word}'


def format_time(time):
    s = time % 60
    m = time // 60 % 60
    h = time // 3600
    return f'{h // 10}{h % 10}:{m // 10}{m % 10}:{s // 10}{s % 10}'


# В будущем можно сделать классом, но
# на данный момент в этом нет необходимости
def get_plot_board(i):
    try:
        with open(path_to_program_data(f'boards/{i}.csv'),
                  'r', encoding='UTF-8') as i_file:
            reader = csv.reader(i_file, delimiter=';', quotechar='"')

            board = []
            for row in reader:
                board.append([*map(lambda x: int(x, 16), row)])

            return board
    except FileNotFoundError:
        return BASE_BOARD_CELLS

