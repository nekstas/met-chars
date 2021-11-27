# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QGridLayout, QTextBrowser

from common.consts import CELLS_V_COUNT, CELLS_H_COUNT
from common.utils import path_to_ui
from core.data.words_list import WordsList
from core.objects.cell import Cell, CellB


class GameScreen(QWidget):
    cells_layout: QGridLayout
    main_display: QTextBrowser
    words_list: WordsList
    level_num: int
    level_word: str
    level_word_d: str

    def __init__(self, words_list, level_num):
        super().__init__()
        uic.loadUi(path_to_ui('screens/game'), self)
        self.init(words_list, level_num)

    def render_word(self):
        # Чтобы текст вертикально был в центре... нужно это
        html = '<font style="font-size: 9pt" color="white"># Чтобы текст был по центру<br></font>'
        self.main_display.setText(html + self.level_word_d)

    def init(self, words_list, level_num):
        self.words_list = words_list
        self.level_num = level_num
        self.level_word = self.words_list.get_word(level_num)
        self.level_word_d = self.level_word.capitalize()

        # Чтобы текст нельзя было выделять...
        self.main_display.setTextInteractionFlags(Qt.NoTextInteraction)

        self.render_word()

        cells_contents = [
            [0x401 | CellB.ENABLED, 0x401 | CellB.ENABLED, 0, 0x276 | CellB.ENABLED],
            [0, 0, 0, 0x289 | CellB.ENABLED],
            [0x801, 0x602, 0, 0x26a | CellB.ENABLED],
            [0, 0x4ff, 0, 0x205 | CellB.ENABLED],
            [0x201 | CellB.ENABLED, 0x202 | CellB.ENABLED, 0x203 | CellB.ENABLED, 0x244 | CellB.ENABLED],
        ]
        for i in range(CELLS_V_COUNT):
            for j in range(CELLS_H_COUNT):
                cell = Cell(cells_contents[i][j])
                self.cells_layout.addWidget(cell, i, j)
