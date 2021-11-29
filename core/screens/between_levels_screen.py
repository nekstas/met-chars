# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton

from common import g
from common.utils import path_to_ui, format_moves_count, format_time
from core.data.words_list import WordsList


class BetweenLevelsScreen(QWidget):
    moves_count_label: QLabel
    time_label: QLabel
    level_num_label: QLabel
    word_label: QLabel
    go_levels_btn: QPushButton
    restart_level_btn: QPushButton
    continue_btn: QPushButton
    show_statistics_btn: QPushButton

    game_mode: str
    level_num: int
    word: str
    words_list: WordsList

    def __init__(self, words_list, level_num, game_mode, moves_count, time_seconds):
        super().__init__()
        uic.loadUi(path_to_ui('screens/between_levels_screen'), self)
        self.init(words_list, level_num, game_mode, moves_count, time_seconds)

    def init(self, words_list, level_num, game_mode, moves_count, time_seconds):
        self.game_mode = game_mode
        self.level_num = level_num
        self.words_list = words_list
        self.word = self.words_list.get_word(level_num)

        self.word_label.setText(self.word.capitalize())

        self.moves_count_label.setText(format_moves_count(moves_count))
        self.level_num_label.setText(f'{self.level_num} уровень')
        self.time_label.setText(format_time(time_seconds))

        self.go_levels_btn.clicked.connect(self.go_levels)
        self.restart_level_btn.clicked.connect(self.restart_level)
        self.continue_btn.clicked.connect(self.continue_game)
        self.show_statistics_btn.clicked.connect(self.show_statistics)

    def go_levels(self):
        from core.screens.plot_level_select import PlotLevelSelectScreen
        from core.screens.random_level_select import RandomLevelSelectScreen

        if self.game_mode == 'p':
            g.window.goto(PlotLevelSelectScreen())
        else:
            g.window.goto(RandomLevelSelectScreen())

    def restart_level(self):
        from core.screens.game import GameScreen

        g.window.goto(GameScreen(self.words_list, self.level_num))

    def continue_game(self):
        from core.screens.game import GameScreen

        g.window.goto(GameScreen(self.words_list, self.level_num + 1))

    def show_statistics(self):
        # TODO: показывать статистику по слову
        pass
