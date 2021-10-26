# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QPushButton

from common import g
from common.utils import path_to_ui


class LevelSelectScreen(QWidget):
    go_back_btn: QPushButton

    def __init__(self):
        super().__init__()
        uic.loadUi(path_to_ui('screens/level_select.ui'), self)
        self.init()

    def init(self):
        pass
        self.go_back_btn.clicked.connect(self.go_back)

    @staticmethod
    def go_back():
        from core.screens.game_mode_select import GameModeSelectScreen
        g.window.goto(GameModeSelectScreen())
