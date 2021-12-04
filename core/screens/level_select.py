# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout

from common import g
from common.sql import SQL
from core.objects.level_item import LevelItem
from ui.screens.level_select import Ui_LevelSelectScreen


class LevelSelectScreen(QWidget, Ui_LevelSelectScreen):
    game_mode_label: QLabel
    continue_btn: QPushButton
    new_game_btn: QPushButton
    go_back_btn: QPushButton
    levels_layout: QVBoxLayout

    game_mode: str
    max_level: int

    def __init__(self, title, game_mode):
        super().__init__()
        self.setupUi(self)
        self.init(title, game_mode)

    def init(self, title, game_mode):
        self.game_mode = game_mode
        self.max_level = -1

        self.game_mode_label.setText(title)
        self.continue_btn.clicked.connect(self.on_continue)
        self.new_game_btn.clicked.connect(self.on_new_game)
        self.go_back_btn.clicked.connect(self.go_back)
        self.levels_layout.setAlignment(Qt.AlignTop)
        self.show_levels()

    def show_levels(self):
        cur = g.db_conn.cursor()
        levels = cur.execute(
            SQL.GET_COMPLETED_LEVELS,
            (g.player_id, self.game_mode)
        ).fetchall()

        if levels:
            for level_num, level_word, level_best_moves, level_best_time in levels:
                self.max_level = max(self.max_level, level_num)
                level_item = LevelItem(
                    level_num, level_word,
                    level_best_moves, level_best_time,
                    self.game_mode
                )
                self.levels_layout.addWidget(level_item)
        else:
            self.continue_btn.hide()

    def delete_completed_levels(self):
        cur = g.db_conn.cursor()
        cur.execute(SQL.DELETE_COMPLETED_LEVELS, (g.player_id, self.game_mode))
        g.db_conn.commit()

    @staticmethod
    def go_back():
        from core.screens.game_mode_select import GameModeSelectScreen
        g.window.goto(GameModeSelectScreen())

    def on_continue(self):
        ...

    def on_new_game(self):
        ...
