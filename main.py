# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
import sys

from PyQt5.QtWidgets import QApplication

from screens.main_window import MainWindow
from screens.menu import MenuScreen

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.goto(MenuScreen())
    window.show()
    sys.exit(app.exec())
