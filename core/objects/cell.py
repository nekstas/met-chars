# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
from PyQt5 import uic
from PyQt5.QtWidgets import QPushButton

from common.utils import path_to_ui
from core.other.cell_b import CellB
from core.other.cell_s import CellS


class Cell(QPushButton):
    code: int
    char: str
    enabled: bool

    button: QPushButton

    def __init__(self, code):
        super().__init__()
        uic.loadUi(path_to_ui('objects/cell.ui'), self)
        self.init(code)

    def init(self, code):
        self.set_code(code)

    def _set_enabled(self):
        self.enabled = bool(self.code & CellB.ENABLED)
        self.setStyleSheet(CellS.CELL_BASE)

    def _set_char(self):
        self.char = ''
        if (self.code & CellB.TYPE) == CellB.ACTION:
            if self.code & CellB.L1:
                self.char += CellB.ACTION_CHARS[(self.code & CellB.L1) >> CellB.L1_SHIFT]
            if self.code & CellB.L2:
                self.char += CellB.ACTION_CHARS[(self.code & CellB.L2) >> CellB.L2_SHIFT]

        self.button.setText(self.char)

    def _set_stylesheet(self):
        stylesheet = CellS.CELL_BASE
        if self.enabled:
            stylesheet += CellS.CELL_ENABLED
        else:
            stylesheet += CellS.CELL_DISABLED
        self.button.setStyleSheet(stylesheet)

    def set_code(self, code):
        self.code = code
        self._set_enabled()
        self._set_char()
        self._set_stylesheet()
