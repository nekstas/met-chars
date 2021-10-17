# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QPushButton

from common import g
from common.utils import path_to_ui
from screens.game import GameScreen


class MenuScreen(QWidget):
    exit_btn: QPushButton
    options_btn: QPushButton
    play_btn: QPushButton

    def __init__(self):
        super().__init__()
        uic.loadUi(path_to_ui('screens/menu.ui'), self)
        self.init()

    def init(self):
        self.exit_btn.clicked.connect(self.on_exit)
        self.play_btn.clicked.connect(self.on_play)

    @staticmethod
    def on_play():
        g.window.goto(GameScreen())

    @staticmethod
    def on_exit():
        g.app.exit()
