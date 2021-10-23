# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
import sqlite3
import sys

from PyQt5.QtWidgets import QApplication

from core.main_window import MainWindow
from common import g
from core.screens.menu import MenuScreen


class App(QApplication):
    window: MainWindow

    def __init__(self):
        super().__init__(sys.argv)
        self.init_db()
        g.app = self

    def init_db(self):
        g.db_conn = sqlite3.connect('db.sqlite')

    @staticmethod
    def create_tables():
        cur = g.db_conn.cursor()
        cur.execute('''
CREATE TABLE IF NOT EXISTS players (int id);''')

    def run(self):
        self.window = MainWindow()
        self.window.goto(MenuScreen())
        self.window.show()
        sys.exit(self.exec())

    def closeAllWindows(self):
        g.db_conn.close()
