# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel

from common import g
from common.utils import path_to_ui


class LevelSelectScreen(QWidget):
    get_levels_sql: str

    game_mode_label: QLabel
    continue_btn: QPushButton
    new_game_btn: QPushButton
    go_back_btn: QPushButton

    def __init__(self, title, get_levels_sql):
        super().__init__()
        uic.loadUi(path_to_ui('screens/level_select'), self)
        self.init(title, get_levels_sql)

    def init(self, title, get_levels_sql):
        self.get_levels_sql = get_levels_sql
        self.game_mode_label.setText(title)
        self.continue_btn.clicked.connect(self.on_continue)
        self.new_game_btn.clicked.connect(self.on_new_game)
        self.go_back_btn.clicked.connect(self.go_back)
        self.levels_layout.setAlignment(Qt.AlignTop)
        self.show_levels()

    def show_levels(self):
        cur = g.db_conn.cursor()
        levels = cur.execute(self.get_levels_sql, (g.player_id, )).fetchall()
        if levels:
            for level in levels:
                # level_item = LevelItem(...)
                # self.players_layout.addWidget(level_item)
                pass
        else:
            self.continue_btn.hide()

    def on_new_game(self):
        ...

    def on_continue(self):
        ...

    @staticmethod
    def go_back():
        from core.screens.game_mode_select import GameModeSelectScreen
        g.window.goto(GameModeSelectScreen())
