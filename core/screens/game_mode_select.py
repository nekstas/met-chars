# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton

from common import g
from common.utils import path_to_ui
from core.objects.game_mode_item import GameModeItem
from core.screens.plot_level_select import PlotLevelSelectScreen
from core.screens.random_level_select import RandomLevelSelectScreen


class GameModeSelectScreen(QWidget):
    game_modes_layout: QVBoxLayout
    gm_plot: GameModeItem
    gm_random: GameModeItem
    go_back_btn: QPushButton

    def __init__(self):
        super().__init__()
        uic.loadUi(path_to_ui('screens/game_mode_select'), self)
        self.init()

    def init(self):
        self.gm_plot = GameModeItem(
            title='Сюжетный режим',
            description='* Определённый порядок слов, от простых к сложным.\n'
                        '* Разные стартовые игровые поля для разных уровней.',
            on_select=self.go_plot_level_select
        )
        self.gm_random = GameModeItem(
            title='Случайный режим',
            description='* Много слов.\n'
                        '* Случайный порядок слов.\n'
                        '* Универсальое стартовое игровое поле для разных уровней.',
            on_select=self.go_random_level_select
        )
        self.game_modes_layout.addWidget(self.gm_plot)
        self.game_modes_layout.addWidget(self.gm_random)
        self.go_back_btn.clicked.connect(self.go_back)

    @staticmethod
    def go_plot_level_select():
        g.window.goto(PlotLevelSelectScreen())

    @staticmethod
    def go_random_level_select():
        g.window.goto(RandomLevelSelectScreen())

    @staticmethod
    def go_back():
        from core.screens.menu import MenuScreen
        g.window.goto(MenuScreen())
