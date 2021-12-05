# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
import random

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QInputDialog, QPushButton, QVBoxLayout

from common import g
from common.consts import PLAYER_NAME_MAX_LEN
from common.save import save_player
from common.sql import SQL
from common.utils import path_to_ui
from core.objects.player_item import PlayerItem


class PlayersScreen(QWidget):
    create_player_btn: QPushButton
    go_back_btn: QPushButton
    players_layout: QVBoxLayout

    def __init__(self):
        super().__init__()
        uic.loadUi(path_to_ui('screens/players'), self)
        self.init()

    def init(self):
        self.create_player_btn.clicked.connect(self.create_player)
        self.go_back_btn.clicked.connect(self.go_back)
        self.players_layout.setAlignment(Qt.AlignTop)
        self.show_players()

    def show_players(self):
        cur = g.db_conn.cursor()
        players = cur.execute(SQL.GET_PLAYERS).fetchall()
        if players:
            for player in players:
                player_item = PlayerItem(player[0], player[1], player[2])
                self.players_layout.addWidget(player_item)
        else:
            print('Что-то пошло не так...')  # O_o

    @staticmethod
    def go_back():
        from core.screens.menu import MenuScreen
        g.window.goto(MenuScreen())

    @staticmethod
    def request_player_name(widget, msg, ok_required=True):
        error = ''
        while True:
            message = msg
            if error:
                message = f'Ошибка: {error}\n{message}'

            player_name, ok_pressed = QInputDialog.getText(
                widget, msg, message
            )

            if not ok_pressed:
                if not ok_required:
                    return player_name, ok_pressed
                error = 'необходимо нажать кнопку ОК!'
            elif not player_name:
                error = 'имя игрока не может быть пустым!'
            elif len(player_name) > PLAYER_NAME_MAX_LEN:
                error = f'имя игрока слишком длинное! ' \
                        f'(больше {PLAYER_NAME_MAX_LEN} символов)'
            else:
                return player_name, ok_pressed

    @staticmethod
    def find_player(widget):
        if g.player_id != -1 and g.player_name is not None:
            return

        cur = g.db_conn.cursor()
        if g.player_id != -1:
            player = cur.execute(SQL.GET_PLAYER_NAME_BY_ID, (g.player_id,)).fetchone()
            if player is None:
                g.player_id = -1
            else:
                g.player_name = player[0]
                g.player_rnd = player[1]
                return

        new_player_name, _ = PlayersScreen.request_player_name(
            widget, 'Как Вас называть?'
        )
        new_player_rnd = random.randint(1, 10 ** 9)
        cur.execute(SQL.CREATE_NEW_PLAYER, (new_player_name, new_player_rnd))
        g.player_id = cur.lastrowid
        g.player_name = new_player_name
        g.db_conn.commit()
        save_player()

    def create_player(self):
        cur = g.db_conn.cursor()
        new_player_name, ok_pressed = PlayersScreen.request_player_name(
            self, 'Введите имя нового игрока:', False
        )
        if not ok_pressed:
            return

        new_player_rnd = random.randint(1, 10 ** 9)
        cur.execute(SQL.CREATE_NEW_PLAYER, (new_player_name, new_player_rnd))
        g.db_conn.commit()

        player_item = PlayerItem(cur.lastrowid, new_player_name, new_player_rnd)
        self.players_layout.addWidget(player_item)
