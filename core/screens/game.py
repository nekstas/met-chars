# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QGridLayout

from common.consts import CELLS_V_COUNT, CELLS_H_COUNT
from common.utils import path_to_ui
from core.data.words_list import WordsList
from core.objects.cell import Cell, CellB


class GameScreen(QWidget):
    cells_layout: QGridLayout
    words_list: WordsList

    def __init__(self, words_list):
        super().__init__()
        uic.loadUi(path_to_ui('screens/game'), self)
        self.init(words_list)

    def init(self, words_list):
        self.words_list = words_list
        for i in range(5):
            print(self.words_list.get_word(i))

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
