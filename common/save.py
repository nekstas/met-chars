# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
from common import g
from common.consts import PLAYER_FILE
from common.utils import path_to_user_data


def save_player():
    with open(path_to_user_data(PLAYER_FILE), 'w') as user_file:
        print(g.player_id, file=user_file)
