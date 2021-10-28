# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QInputDialog

from common.consts import PLAYER_NAME_MAX_LEN
from common.utils import path_to_ui


class PlayersScreen(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(path_to_ui('screens/players.ui'), self)
        self.init()

    def init(self):
        pass

    @staticmethod
    def request_player_name(widget, msg):
        error = ''
        while True:
            message = msg
            if error:
                message = f'Ошибка: {error}\n{message}'

            player_name, ok_pressed = QInputDialog.getText(
                widget, msg, message
            )

            if not ok_pressed:
                error = 'необходимо нажать кнопку ОК!'
            elif not player_name:
                error = 'имя игрока не может быть пустым!'
            elif len(player_name) > PLAYER_NAME_MAX_LEN:
                error = f'имя игрока слишком длинное! ' \
                        f'(больше {PLAYER_NAME_MAX_LEN} символов)'
            else:
                return player_name
