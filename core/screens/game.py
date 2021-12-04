# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
from typing import Optional

from PyQt5 import uic
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QWidget, QGridLayout, QTextBrowser, QLabel, QPushButton

from common import g
from common.consts import CELLS_V_COUNT, CELLS_H_COUNT, BASE_BOARD_CELLS
from common.sql import SQL
from common.utils import path_to_ui, format_time, format_moves_count, get_plot_board
from core.data.plot_words_list import PlotWordsList
from core.data.words_list import WordsList
from core.objects.cell import Cell, CellB
from core.screens.between_levels_screen import BetweenLevelsScreen
from core.screens.game_over import GameOverScreen


class GameScreen(QWidget):
    cells_layout: QGridLayout
    main_display: QTextBrowser
    sub_display: QLabel
    words_list: WordsList
    moves_count_label: QLabel
    level_num_label: QLabel
    time_label: QLabel
    go_back_btn: QPushButton
    restart_level_btn: QPushButton
    level_timer: QTimer

    game_mode: str
    level_num: int
    word: str
    word_d: str
    moves_count: int
    time_seconds: int

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

    def save_level_completed(self):
        cur = g.db_conn.cursor()

        check_res = cur.execute(
            SQL.CHECK_COMPLETED_LEVEL,
            (g.player_id, self.level_num, self.game_mode)
        ).fetchone()

        if check_res is None:
            cur.execute(
                SQL.ADD_COMPLETED_LEVEL,
                (
                    g.player_id, self.word, self.game_mode, self.level_num,
                    self.moves_count, self.time_seconds
                )
            )
        else:
            cur.execute(
                SQL.UPDATE_COMPLETED_LEVEL,
                (
                    self.moves_count, self.time_seconds,
                    g.player_id, self.level_num, self.game_mode
                )
            )

        g.db_conn.commit()

    def save_statistics(self):
        cur = g.db_conn.cursor()

        cur.execute(
            SQL.ADD_WORD_STATISTICS,
            (
                g.player_id, self.word, self.game_mode,
                self.moves_count, self.time_seconds
            )
        )

        g.db_conn.commit()

    def check_level_end(self):
        if self.char_i != len(self.word):
            return

        self.save_level_completed()
        self.save_statistics()

        g.window.goto(BetweenLevelsScreen(
            self.words_list, self.level_num, self.game_mode,
            self.moves_count, self.time_seconds,
        ))

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

    def render_status(self):
        self.moves_count_label.setText(format_moves_count(self.moves_count))
        self.level_num_label.setText(f'{self.level_num} уровень')
        self.time_label.setText(format_time(self.time_seconds))

    def create_board(self):
        if self.game_mode == 'r':
            cells = BASE_BOARD_CELLS
        else:
            cells = get_plot_board(self.level_num)

        for i in range(CELLS_V_COUNT):
            for j in range(CELLS_H_COUNT):
                cell = Cell(cells[i][j], self.on_cell_clicked)
                self.cells_layout.addWidget(cell, i, j)

    def on_cell_char_clicked(self, cell):
        if self.char_i >= len(self.word):
            return  # o_O

        self.moves_count += 1
        if self.word[self.char_i] == cell.get_char():
            self.char_i += 1
            self.char_ok = True
        else:
            self.char_ok = False

        self.render_word()
        self.render_status()
        self.check_level_end()

    def on_cell_num_clicked(self, cell):
        if self.cell1 is None:
            self.cell1 = cell
        elif self.cell2 is not None:
            if self.cell2.get_act() in {'//', '%'} and cell.get_num() == 0:
                self.zero_division_error = True
                self.cell1 = self.cell2 = None
            elif self.cell1 != cell:
                self.cell3 = cell

        self.render_preview()

    def on_cell_not_act_clicked(self, cell):
        if self.cell1 is None and cell.is_letter():
            self.on_cell_char_clicked(cell)
        elif self.cell3 is None and cell.is_num():
            self.on_cell_num_clicked(cell)
        elif self.cell3 is not None:
            self.moves_count += 1
            new_cell = self.cell2.process(self.cell1, self.cell3)
            self.cell1 = self.cell2 = self.cell3 = None
            new_cell.bind_on_clicked(self.on_cell_clicked)
            self.cells_layout.replaceWidget(cell, new_cell)
            self.render_preview()
            self.render_status()

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
                self.moves_count += 1
                new_cell.bind_on_clicked(self.on_cell_clicked)
                self.cells_layout.replaceWidget(self.cell1, new_cell)
                self.cell1 = None

        self.render_preview()
        self.render_status()

    def on_cell_clicked(self, cell):
        if not cell.is_enabled():
            return

        if cell.is_act():
            self.on_cell_act_clicked(cell)
        else:
            self.on_cell_not_act_clicked(cell)

    def every_second(self):
        self.time_seconds += 1
        self.render_status()

    def go_back(self):
        from core.screens.plot_level_select import PlotLevelSelectScreen
        from core.screens.random_level_select import RandomLevelSelectScreen

        if self.game_mode == 'p':
            g.window.goto(PlotLevelSelectScreen())
        else:
            g.window.goto(RandomLevelSelectScreen())

    def restart_level(self):
        g.window.goto(GameScreen(self.words_list, self.level_num))

    def init(self, words_list, level_num):
        self.words_list = words_list
        self.game_mode = 'p' if isinstance(self.words_list, PlotWordsList) else 'r'
        self.level_num = level_num

        self.word = self.words_list.get_word(level_num)
        if self.word is None:
            g.window.goto(GameOverScreen(self.game_mode), p=2)
            return

        self.word_d = self.word.capitalize()
        self.moves_count = 0
        self.time_seconds = 0

        self.char_i = 0
        self.char_ok = True
        self.cell1 = self.cell2 = self.cell3 = None
        self.zero_division_error = False

        self.go_back_btn.clicked.connect(self.go_back)
        self.restart_level_btn.clicked.connect(self.restart_level)

        # Чтобы текст нельзя было выделять...
        self.main_display.setTextInteractionFlags(Qt.NoTextInteraction)

        self.level_timer = QTimer(self)
        self.level_timer.timeout.connect(self.every_second)
        self.level_timer.start(1000)

        self.render_word()
        self.render_preview()
        self.render_status()
        self.create_board()
