# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
import os
import sqlite3
import sys

from PyQt5.QtWidgets import QApplication

from common import g
from common.consts import PATH_TO_USER_DATA, PLAYER_FILE, DB_FILE
from common.sql import SQL
from common.utils import path_to_user_data
from core.main_window import MainWindow
from core.screens.menu import MenuScreen


class App(QApplication):
    window: MainWindow

    def __init__(self):
        super().__init__(sys.argv)
        g.app = self
        self.init()

    def init(self):
        self.init_db()
        self.load_user_data()

    def init_db(self):
        g.db_conn = sqlite3.connect(path_to_user_data(DB_FILE))
        self.create_tables()

    @staticmethod
    def load_user_data():
        if not os.path.exists(PATH_TO_USER_DATA):
            os.mkdir(PATH_TO_USER_DATA)

        if os.path.exists(path_to_user_data(PLAYER_FILE)):
            with open(path_to_user_data(PLAYER_FILE), 'r') as user_file:
                player_id_str = user_file.readline().strip()
                if player_id_str.isdigit():
                    g.player_id = int(player_id_str)

    @staticmethod
    def create_tables():
        cur = g.db_conn.cursor()

        cur.execute(SQL.CREATE_TABLE_PLAYERS)
        cur.execute(SQL.CREATE_TABLE_COMPLETED_LEVELS)

        g.db_conn.commit()

    def run(self):
        self.window = MainWindow()
        self.window.goto(MenuScreen())
        self.window.show()
        sys.exit(self.exec())

    def closeAllWindows(self):
        g.db_conn.close()
