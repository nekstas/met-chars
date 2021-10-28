# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel

from common import g
from common.consts import PLAYER_FILE
from common.sql import SQL
from common.utils import path_to_ui, path_to_user_data
from core.screens.game_mode_select import GameModeSelectScreen
from core.screens.players import PlayersScreen


class MenuScreen(QWidget):
    exit_btn: QPushButton
    players_btn: QPushButton
    play_btn: QPushButton
    player_name_label: QLabel

    def __init__(self):
        super().__init__()
        uic.loadUi(path_to_ui('screens/menu.ui'), self)
        self.init()

    def find_player(self):
        cur = g.db_conn.cursor()
        if g.player_id != -1:
            player = cur.execute(SQL.GET_PLAYER_NAME_BY_ID, (g.player_id, )).fetchone()
            if player is None:
                g.player_id = -1
            else:
                g.player_name = player[0]
                return

        new_player_name = PlayersScreen.request_player_name(
            self, 'Как Вас называть?'
        )
        cur.execute(SQL.CREATE_NEW_PLAYER, (new_player_name, ))
        g.player_id = cur.lastrowid
        g.player_name = new_player_name
        g.db_conn.commit()

        with open(path_to_user_data(PLAYER_FILE), 'w') as user_file:
            print(g.player_id, file=user_file)

    def init(self):
        self.find_player()
        self.player_name_label.setText(f'Игрок: {g.player_name}')
        self.exit_btn.clicked.connect(self.on_exit)
        self.play_btn.clicked.connect(self.on_play)
        self.players_btn.clicked.connect(self.on_players)

    @staticmethod
    def on_play():
        g.window.goto(GameModeSelectScreen())

    @staticmethod
    def on_players():
        g.window.goto(PlayersScreen())

    @staticmethod
    def on_exit():
        g.app.exit()
