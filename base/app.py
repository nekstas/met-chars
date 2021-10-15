# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
import sys

from PyQt5.QtWidgets import QApplication

from base.main_window import MainWindow
from screens.menu import MenuScreen


class App(QApplication):
    def __init__(self):
        super().__init__(sys.argv)

    def run(self):
        window = MainWindow(self)
        window.goto(MenuScreen())
        window.show()
        sys.exit(self.exec())
