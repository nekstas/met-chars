# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
from PyQt5.QtWidgets import QMainWindow

from consts.consts import PROJECT_NAME


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_program()

    def init_program(self):
        self.setGeometry(400, 400, 400, 400)
        self.setWindowTitle(PROJECT_NAME)
