# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton

from common import g
from common.utils import format_moves_count, format_time
from core.data.plot_words_list import PlotWordsList
from core.data.random_words_list import RandomWordsList
from core.screens.game import GameScreen
from core.screens.statistics import StatisticsScreen
from ui.objects.level_item import Ui_LevelItem


class LevelItem(QWidget, Ui_LevelItem):
    level_word_label: QLabel
    best_moves_count_label: QLabel
    level_num_label: QLabel
    best_time_label: QLabel
    play_level_btn: QPushButton
    show_statistics_btn: QPushButton

    level_num: int
    level_word: str
    game_mode: str

    def __init__(self, level_num, level_word, level_best_moves, level_best_time,
                 game_mode):
        super().__init__()
        self.setupUi(self)
        self.init(level_num, level_word, level_best_moves, level_best_time, game_mode)

    def init(self, level_num, level_word, level_best_moves, level_best_time, game_mode):
        self.level_num = level_num
        self.level_word = level_word
        self.game_mode = game_mode

        self.level_word_label.setText(level_word.capitalize())

        self.best_moves_count_label.setText(format_moves_count(level_best_moves))
        self.level_num_label.setText(f'{self.level_num} уровень')
        self.best_time_label.setText(format_time(level_best_time))

        self.play_level_btn.clicked.connect(self.play_level)
        self.show_statistics_btn.clicked.connect(self.show_statistics)

    def play_level(self):
        if self.game_mode == 'p':
            g.window.goto(GameScreen(PlotWordsList(), self.level_num))
        else:
            g.window.goto(GameScreen(RandomWordsList(), self.level_num))

    def show_statistics(self):
        from core.screens.plot_level_select import PlotLevelSelectScreen
        from core.screens.random_level_select import RandomLevelSelectScreen
        if self.game_mode == 'p':
            g.window.goto(StatisticsScreen('p', self.level_word, PlotLevelSelectScreen))
        else:
            g.window.goto(StatisticsScreen('r', self.level_word, RandomLevelSelectScreen))
