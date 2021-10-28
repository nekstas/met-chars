# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel

from common import g
from common.utils import path_to_ui


class LevelSelectScreen(QWidget):
    game_mode_label: QLabel
    go_back_btn: QPushButton

    def __init__(self, title):
        super().__init__()
        uic.loadUi(path_to_ui('screens/level_select'), self)
        self.init(title)

    def init(self, title):
        self.game_mode_label.setText(title)
        self.go_back_btn.clicked.connect(self.go_back)
        self.levels_layout.setAlignment(Qt.AlignTop)

    @staticmethod
    def go_back():
        from core.screens.game_mode_select import GameModeSelectScreen
        g.window.goto(GameModeSelectScreen())
