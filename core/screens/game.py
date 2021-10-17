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
        for i in range(CELLS_V_COUNT):
            for j in range(CELLS_H_COUNT):
                self.cells_layout.addWidget(Cell(), i, j)
