# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
from __future__ import annotations

from PyQt5 import uic
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QPushButton, QWidget

from common.utils import path_to_ui
from core.other.cell_b import CellB
from core.other.cell_s import CellS


class Cell(QWidget):
    button: QPushButton

    code: int
    char: str
    enabled: bool

    def __init__(self, code, on_clicked=None):
        super().__init__()
        uic.loadUi(path_to_ui('objects/cell'), self)
        self.init(code, on_clicked)

    def init(self, code, on_clicked):
        if on_clicked is not None:
            self.button.clicked.connect(lambda: on_clicked(self))
        self.set_code(code)

    def bind_on_clicked(self, on_clicked):
        self.button.clicked.connect(lambda: on_clicked(self))

    def get_type(self):
        return self.code & CellB.TYPE

    def is_free(self):
        return self.get_type() == CellB.FREE

    def is_act(self):
        return self.get_type() == CellB.ACTION

    def is_enabled(self):
        return self.enabled

    def is_letter(self):
        return self.get_type() in {CellB.CHAR_RU, CellB.CHAR_EN}

    def is_num(self):
        return self.get_type() == CellB.NUMBER

    def get_num(self):
        return self.code & CellB.DATA

    def has_data(self):
        return not self.is_free() and not self.is_act()

    def get_char(self):
        return self.char.lower()

    def get_act(self):
        return self.char

    def _set_enabled(self):
        self.enabled = bool(self.code & CellB.ENABLED)

    def _set_char(self):
        self.char = ''
        if (self.code & CellB.TYPE) == CellB.ACTION:
            if self.code & CellB.L1:
                self.char += CellB.ACTION_CHARS[(self.code & CellB.L1) >> CellB.L1_SHIFT]
            if self.code & CellB.L2:
                self.char += CellB.ACTION_CHARS[(self.code & CellB.L2) >> CellB.L2_SHIFT]
        elif (self.code & CellB.TYPE) == CellB.NUMBER:
            self.char = str(self.code & CellB.DATA)
        elif (self.code & CellB.TYPE) == CellB.CHAR_RU:
            self.char = CellB.RU_CHARS[(self.code & CellB.DATA) - 1]
        elif (self.code & CellB.TYPE) == CellB.CHAR_EN:
            self.char = CellB.EN_CHARS[(self.code & CellB.DATA) - 1]

        self.button.setText(self.char)

    def _set_style(self):
        font = QFont('Segoe UI', CellS.FONT_SIZES[len(self.char)], 75)
        font.setBold(True)
        self.button.setFont(font)

        stylesheet = CellS.BASE
        if self.enabled:
            stylesheet += CellS.ENABLED
        else:
            stylesheet += CellS.DISABLED

        self.setStyleSheet(stylesheet)
        self.button.setStyleSheet(stylesheet)

    def set_code(self, code):
        self.code = code
        self._set_enabled()
        self._set_char()
        self._set_style()

    def process(self, cell1, cell2):
        if self.get_act() == '+':
            return cell1 + cell2
        elif self.get_act() == '−':
            return cell1 - cell2
        elif self.get_act() == '×':
            return cell1 * cell2
        elif self.get_act() == '//':
            return cell1 // cell2
        elif self.get_act() == '%':
            return cell1 % cell2
        # o_O

    @staticmethod
    def create_num(num):
        num %= 256
        return Cell(num | CellB.NUMBER | CellB.ENABLED)

    def __add__(self, cell2):
        return Cell.create_num(self.get_num() + cell2.get_num())

    def __sub__(self, cell2):
        return Cell.create_num(self.get_num() - cell2.get_num())

    def __mul__(self, cell2):
        return Cell.create_num(self.get_num() * cell2.get_num())

    def __mod__(self, cell2):
        return Cell.create_num(self.get_num() % cell2.get_num())

    def __floordiv__(self, cell2):
        return Cell.create_num(self.get_num() // cell2.get_num())

    def to_char(self, t):
        if t == CellB.CHAR_RU and (self.get_num() < 1 or
                                   self.get_num() > len(CellB.RU_CHARS)):
            return
        if t == CellB.CHAR_EN and (self.get_num() < 1 or
                                   self.get_num() > len(CellB.EN_CHARS)):
            return

        return Cell(self.get_num() | t | CellB.ENABLED)
