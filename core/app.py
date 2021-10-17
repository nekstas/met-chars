# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
import sys

from PyQt5.QtWidgets import QApplication

from core.main_window import MainWindow
from common import g
from screens.menu import MenuScreen


class App(QApplication):
    window: MainWindow

    def __init__(self):
        super().__init__(sys.argv)
        g.app = self

    def run(self):
        self.window = MainWindow()
        self.window.goto(MenuScreen())
        self.window.show()
        sys.exit(self.exec())
