# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton

from common import g
from ui.screens.game_over import Ui_GameOverScreen


class GameOverScreen(QWidget, Ui_GameOverScreen):
    game_over_text_label: QLabel
    go_levels_btn: QPushButton
    exit_btn: QPushButton

    game_mode: str

    def __init__(self, game_mode):
        super().__init__()
        self.setupUi(self)
        self.init(game_mode)

    def init(self, game_mode):
        self.game_mode = game_mode

        self.game_over_text_label.setText(
            '''Поздравляю!
Вы прошли игру Met Chars. Надеюсь, Вам понравилось!
Вы также можете перепроходить уровни и ставить новые рекорды.
Спасибо за прохождение!'''
        )

        self.go_levels_btn.clicked.connect(self.go_levels)
        self.exit_btn.clicked.connect(self.on_exit)

    def go_levels(self):
        from core.screens.plot_level_select import PlotLevelSelectScreen
        from core.screens.random_level_select import RandomLevelSelectScreen

        if self.game_mode == 'p':
            g.window.goto(PlotLevelSelectScreen(), anyway=True)
        else:
            g.window.goto(RandomLevelSelectScreen(), anyway=True)

    @staticmethod
    def on_exit():
        g.app.exit()
