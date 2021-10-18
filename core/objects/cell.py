# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
from PyQt5 import uic
from PyQt5.QtWidgets import QPushButton

from common.utils import path_to_ui


class Cell(QPushButton):
    def __init__(self):
        super().__init__()
        uic.loadUi(path_to_ui('objects/cell.ui'), self)
        self.init()

    def init(self):
        pass
