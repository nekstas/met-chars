# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
from typing import Tuple, Any

from PyQt5.QtWidgets import QWidget, QLabel, QTableWidget, QRadioButton, \
    QCheckBox, QPushButton, QTableWidgetItem

from common import g
from common.sql import SQL
from common.utils import format_time
from ui.screens.statistics import Ui_StatisticsScreen


class StatisticsScreen(QWidget, Ui_StatisticsScreen):
    word_label: QLabel
    statistics_table: QTableWidget
    by_moves_rb: QRadioButton
    by_time_rb: QRadioButton
    only_best_results_checkbox: QCheckBox
    go_back_btn: QPushButton

    game_mode: str
    word: str
    back_screen: Any
    back_args: Tuple
    only_best_results: bool
    sort_arg: str

    def __init__(self, game_mode, word, back_screen, *back_args):
        super().__init__()
        self.setupUi(self)
        self.init(game_mode, word, back_screen, back_args)

    def render_statistics(self):
        if self.only_best_results:
            if self.sort_arg == 'moves':
                query = SQL.GET_WORD_STATISTICS_ONLY_BEST_MOVES
            else:
                query = SQL.GET_WORD_STATISTICS_ONLY_BEST_TIME
        elif self.sort_arg == 'moves':
            query = SQL.GET_WORD_STATISTICS_MOVES
        else:
            query = SQL.GET_WORD_STATISTICS_TIME

        cur = g.db_conn.cursor()
        statistics = cur.execute(
            query, (self.game_mode, self.word)
        ).fetchall()

        self.statistics_table.clearContents()

        self.statistics_table.setRowCount(len(statistics))
        for i, (name, moves_count, time_seconds) in enumerate(statistics):
            self.statistics_table.setItem(
                i, 0, QTableWidgetItem(name)
            )
            self.statistics_table.setItem(
                i, 1, QTableWidgetItem(str(moves_count))
            )
            self.statistics_table.setItem(
                i, 2, QTableWidgetItem(format_time(time_seconds))
            )

    def init(self, game_mode, word, back_screen, back_args):
        self.game_mode = game_mode
        self.word = word
        self.back_screen = back_screen
        self.back_args = back_args

        self.word_label.setText(self.word.capitalize())
        self.statistics_table.setColumnWidth(0, 190)
        self.statistics_table.setColumnWidth(1, 50)
        self.statistics_table.setColumnWidth(2, 70)

        self.only_best_results = self.only_best_results_checkbox.isChecked()
        self.sort_arg = 'moves' if self.by_moves_rb.isChecked() else 'time'

        self.only_best_results_checkbox.clicked.connect(self.on_change)
        self.by_moves_rb.clicked.connect(self.on_change)
        self.by_time_rb.clicked.connect(self.on_change)

        self.go_back_btn.clicked.connect(self.go_back)

        self.render_statistics()

    def on_change(self):
        self.only_best_results = self.only_best_results_checkbox.isChecked()
        self.sort_arg = 'moves' if self.by_moves_rb.isChecked() else 'time'

        self.render_statistics()

    def go_back(self):
        g.window.goto(self.back_screen(*self.back_args))
