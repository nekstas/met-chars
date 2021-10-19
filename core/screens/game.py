# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QGridLayout

from common.consts import CELLS_V_COUNT, CELLS_H_COUNT
from common.utils import path_to_ui
from core.objects.cell import Cell


class GameScreen(QWidget):
    cells_layout: QGridLayout

    def __init__(self):
        super().__init__()
        uic.loadUi(path_to_ui('screens/game.ui'), self)
        self.init()

    def init(self):
        cells_contents = [
            [0, 0, 0, 0x365],
            [0, 0, 0, 0x378],
            [0, 0, 0, 0x359],
            [0, 0, 0, 0],
            [0x301, 0x302, 0x303, 0x304],
        ]
        for i in range(CELLS_V_COUNT):
            for j in range(CELLS_H_COUNT):
                cell = Cell(cells_contents[i][j])
                self.cells_layout.addWidget(cell, i, j)
