# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
from typing import Optional

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QGridLayout, QTextBrowser, QLabel

from common import g
from common.consts import CELLS_V_COUNT, CELLS_H_COUNT
from common.utils import path_to_ui
from core.data.words_list import WordsList
from core.objects.cell import Cell, CellB


class GameScreen(QWidget):
    cells_layout: QGridLayout
    main_display: QTextBrowser
    sub_display: QLabel
    words_list: WordsList
    level_num: int
    word: str
    word_d: str

    char_i: int
    char_ok: bool
    cell1: Optional[Cell]
    cell2: Optional[Cell]
    cell3: Optional[Cell]
    zero_division_error: bool

    def __init__(self, words_list, level_num):
        super().__init__()
        uic.loadUi(path_to_ui('screens/game'), self)
        self.init(words_list, level_num)

    def check_level_end(self):
        # TODO: сделать нормальное окончание уровня
        if self.char_i == len(self.word):
            g.window.goto(GameScreen(self.words_list, self.level_num + 1))

    def render_word(self):
        # Чтобы текст вертикально был в центре... нужно это
        html = '<font style="font-size: 9pt" color="white"># Чтобы текст был по центру<br></font>'

        for i, char in enumerate(self.word_d):
            if i < self.char_i:
                color = '#3da842'  # Верно отмеченные символы, Зелёный
            elif i == self.char_i:
                char = f'<b>{char}</b>'  # Текущий символ, жирный.
                if self.char_ok:
                    color = '#8e72e8'  # Нужно нажать, Фиолетовый
                else:
                    color = '#a8423d'  # Пытались нажать, неправильно, Красный
            else:
                color = '#000000'  # Следующие символы, Чёрный

            html += f'<font color="{color}">{char}</font>'

        self.main_display.setHtml(html)

    def render_preview(self):
        parts = []
        if self.zero_division_error:
            self.zero_division_error = False
            parts.append('Нельзя делить на 0!')
        else:
            if self.cell1 is not None:
                parts.append(self.cell1.get_char())
            if self.cell2 is not None:
                parts.append(self.cell2.get_char())
            if self.cell3 is not None:
                parts.append(self.cell3.get_char())
                parts.append('=')
                parts.append(self.cell2.process(self.cell1, self.cell3).get_char())

        text = ' '.join(parts)
        self.sub_display.setText(text)

    def create_board(self):
        # cells_contents = [
        #     [0x401 | CellB.ENABLED, 0x401 | CellB.ENABLED, CellB.ENABLED, 0x276 | CellB.ENABLED],
        #     [0, 0, 0, 0x289 | CellB.ENABLED],
        #     [0x601 | CellB.ENABLED, 0x602 | CellB.ENABLED, 0, 0x26a | CellB.ENABLED],
        #     [0, 0x4ff, 0, 0x205 | CellB.ENABLED],
        #     [0x201 | CellB.ENABLED, 0x202 | CellB.ENABLED, 0x203 | CellB.ENABLED, 0x244 | CellB.ENABLED],
        # ]

        cells_contents = [
            [0x401 | CellB.ENABLED, 0x401 | CellB.ENABLED, CellB.ENABLED, 0x276 | CellB.ENABLED],
            [CellB.ENABLED, CellB.ENABLED, CellB.ENABLED, 0x289 | CellB.ENABLED],
            [0, 0, 0, 0x26a | CellB.ENABLED],
            [CellB.ENABLED, CellB.ENABLED, CellB.ENABLED, 0x205 | CellB.ENABLED],
            [0x201 | CellB.ENABLED, 0x202 | CellB.ENABLED, 0x203 | CellB.ENABLED, 0x244 | CellB.ENABLED],
        ]
        # TODO: сделать разное стартовое игровое поле для разных уровней из сюжетного режима

        for i in range(CELLS_V_COUNT):
            for j in range(CELLS_H_COUNT):
                cell = Cell(cells_contents[i][j], self.on_cell_clicked)
                self.cells_layout.addWidget(cell, i, j)

    def on_cell_char_clicked(self, cell):
        if self.char_i >= len(self.word):
            return  # o_O

        if self.word[self.char_i] == cell.get_char():
            self.char_i += 1
            self.char_ok = True
        else:
            self.char_ok = False

        self.render_word()
        self.check_level_end()

    def on_cell_num_clicked(self, cell):
        if self.cell1 is None:
            self.cell1 = cell
        elif self.cell2 is not None:
            if self.cell2.get_act() in {'//', '%'} and cell.get_num() == 0:
                self.zero_division_error = True
                self.cell1 = self.cell2 = None
            else:
                self.cell3 = cell

        self.render_preview()

    def on_cell_not_act_clicked(self, cell):
        if self.cell1 is None and cell.is_letter():
            self.on_cell_char_clicked(cell)
        elif self.cell3 is None and cell.is_num():
            self.on_cell_num_clicked(cell)
        elif self.cell3 is not None:
            new_cell = self.cell2.process(self.cell1, self.cell3)
            self.cell1 = self.cell2 = self.cell3 = None
            new_cell.bind_on_clicked(self.on_cell_clicked)
            self.cells_layout.replaceWidget(cell, new_cell)
            self.render_preview()

    def on_cell_act_clicked(self, cell):
        if cell.get_act() in {'+', '−', '×', '//', "%"}:
            if self.cell1 is not None and self.cell3 is None:
                self.cell2 = cell
        elif cell.get_act() == 'CE':
            self.cell1 = self.cell2 = self.cell3 = None
            self.zero_division_error = False
        elif self.cell1 is not None and self.cell2 is None:
            new_cell = None
            if cell.get_act() == 'RU':
                new_cell = self.cell1.to_char(CellB.CHAR_RU)
            elif cell.get_act() == 'EN':
                new_cell = self.cell1.to_char(CellB.CHAR_EN)

            if new_cell is not None:
                new_cell.bind_on_clicked(self.on_cell_clicked)
                self.cells_layout.replaceWidget(self.cell1, new_cell)
                self.cell1 = None

        self.render_preview()

    def on_cell_clicked(self, cell):
        if not cell.is_enabled():
            return

        if cell.is_act():
            self.on_cell_act_clicked(cell)
        else:
            self.on_cell_not_act_clicked(cell)

    def init(self, words_list, level_num):
        self.words_list = words_list
        self.level_num = level_num
        self.word = self.words_list.get_word(level_num)
        self.word_d = self.word.capitalize()

        self.char_i = 0
        self.char_ok = True
        self.cell1 = self.cell2 = self.cell3 = None
        self.zero_division_error = False

        # Чтобы текст нельзя было выделять...
        self.main_display.setTextInteractionFlags(Qt.NoTextInteraction)

        self.render_word()
        self.create_board()
