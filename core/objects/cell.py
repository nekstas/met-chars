# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
from PyQt5 import uic
from PyQt5.QtWidgets import QPushButton

from common.utils import path_to_ui


class CellB:
    ACTION_CHARS = ' +-*/ECRUN'

    DATA, IS_ENABLED, TYPE = 0xFF, 0x100, 0xE00

    L1, L1_SHIFT = 0xF0, 4
    L2, L2_SHIFT = 0xF, 0

    DISABLED, ENABLED = 0, 0x100

    FREE, ACTION, NUMBER, CHAR_RU, CHAR_EN = 0, 0x200, 0x400, 0x600, 0x800


class Cell(QPushButton):
    code: int
    char: str

    button: QPushButton

    def __init__(self, code):
        super().__init__()
        uic.loadUi(path_to_ui('objects/cell.ui'), self)
        self.set_code(code)
        self.init()

    def init(self):
        self.button.setText(self.char)

    def set_code(self, code):
        self.code = code
        self.char = ''
        if (self.code & CellB.TYPE) == CellB.ACTION:
            if self.code & CellB.L1:
                self.char += CellB.ACTION_CHARS[(self.code & CellB.L1) >> CellB.L1_SHIFT]
            if self.code & CellB.L2:
                self.char += CellB.ACTION_CHARS[(self.code & CellB.L2) >> CellB.L2_SHIFT]
