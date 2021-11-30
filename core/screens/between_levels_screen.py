# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
import os
import random

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton

from common import g
from common.utils import path_to_ui, format_moves_count, format_time, path_to_program_data
from core.data.words_list import WordsList
from core.screens.statistics import StatisticsScreen

MEME_MAX_WIDTH = 340
MEME_MAX_HEIGHT = 369
MEMES_COUNT = len(os.listdir(path_to_program_data('memes/')))


class BetweenLevelsScreen(QWidget):
    moves_count_label: QLabel
    time_label: QLabel
    level_num_label: QLabel
    word_label: QLabel
    go_levels_btn: QPushButton
    restart_level_btn: QPushButton
    continue_btn: QPushButton
    show_statistics_btn: QPushButton
    meme_label: QLabel

    game_mode: str
    level_num: int
    word: str
    moves_count: int
    time_seconds: int
    meme_i: int
    words_list: WordsList

    def __init__(self, words_list, level_num, game_mode, moves_count, time_seconds,
                 meme_i=-1):
        super().__init__()
        uic.loadUi(path_to_ui('screens/between_levels'), self)
        self.init(words_list, level_num, game_mode, moves_count, time_seconds, meme_i)

    def init(self, words_list, level_num, game_mode, moves_count, time_seconds, meme_i):
        self.game_mode = game_mode
        self.level_num = level_num
        self.words_list = words_list
        self.moves_count = moves_count
        self.time_seconds = time_seconds
        self.meme_i = meme_i

        self.word = self.words_list.get_word(level_num)
        self.word_label.setText(self.word.capitalize())

        self.moves_count_label.setText(format_moves_count(moves_count))
        self.level_num_label.setText(f'{self.level_num} уровень')
        self.time_label.setText(format_time(time_seconds))

        self.go_levels_btn.clicked.connect(self.go_levels)
        self.restart_level_btn.clicked.connect(self.restart_level)
        self.continue_btn.clicked.connect(self.continue_game)
        self.show_statistics_btn.clicked.connect(self.show_statistics)

        if self.meme_i == -1:
            self.meme_i = random.randint(0, MEMES_COUNT - 1)

        meme_pixmap = QPixmap(path_to_program_data(f'memes/{self.meme_i}.jpg'))
        meme_pixmap = meme_pixmap.scaled(
            MEME_MAX_WIDTH, MEME_MAX_HEIGHT, Qt.KeepAspectRatio
        )

        self.meme_label.setPixmap(meme_pixmap)

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
        g.window.goto(StatisticsScreen(
            self.game_mode, self.word,
            BetweenLevelsScreen,
            self.words_list, self.level_num, self.game_mode,
            self.moves_count, self.time_seconds, self.meme_i
        ))
