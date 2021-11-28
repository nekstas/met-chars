# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton

from common import g
from common.save import save_player
from common.sql import SQL
from common.utils import path_to_ui


class PlayerItem(QWidget):
    player_id: int
    player_name: str
    player_rnd: int

    player_name_label: QLabel
    selected_label: QLabel
    select_btn: QPushButton
    change_name_btn: QPushButton
    delete_btn: QPushButton

    def __init__(self, player_id, player_name, player_rnd):
        super().__init__()
        uic.loadUi(path_to_ui('objects/player_item'), self)
        self.init(player_id, player_name, player_rnd)

    def update_view(self):
        self.player_name_label.setText(self.player_name)
        if self.player_id == g.player_id:
            self.selected_label.show()
            self.select_btn.hide()
            self.delete_btn.hide()
        else:
            self.selected_label.hide()
            self.select_btn.show()
            self.delete_btn.show()

    def init(self, player_id, player_name, player_rnd):
        self.player_id = player_id
        self.player_name = player_name
        self.player_rnd = player_rnd

        self.update_view()

        self.select_btn.clicked.connect(self.on_select_clicked)
        self.change_name_btn.clicked.connect(self.on_change_name)
        self.delete_btn.clicked.connect(self.on_delete_clicked)

    def on_select_clicked(self):
        from core.screens.players import PlayersScreen
        g.player_id = self.player_id
        g.player_name = self.player_name
        g.player_rnd = self.player_rnd
        save_player()

        # PyQt почему-то тут не очень умный...
        # Поэтому приходится обновлять весь экран, а не два виджета
        g.window.goto(PlayersScreen())

    def on_change_name(self):
        from core.screens.players import PlayersScreen
        cur = g.db_conn.cursor()
        player_new_name, ok_pressed = PlayersScreen.request_player_name(
            self, 'Введите новое имя для игрока:', False
        )
        if not ok_pressed:
            return

        cur.execute(SQL.CHANGE_PLAYER_NAME, (player_new_name, self.player_id, ))
        g.db_conn.commit()

        self.player_name = player_new_name
        if self.player_id == g.player_id:
            g.player_name = self.player_name
        self.update_view()

    def on_delete_clicked(self):
        from core.screens.players import PlayersScreen
        cur = g.db_conn.cursor()
        cur.execute(SQL.DELETE_PLAYER, (self.player_id, ))
        g.db_conn.commit()

        # Тут также
        g.window.goto(PlayersScreen())
