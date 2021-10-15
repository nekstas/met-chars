# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
import sys

from PyQt5.QtWidgets import QApplication

from windows.main import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
