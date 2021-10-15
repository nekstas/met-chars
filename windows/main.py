# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

from common.utils import path_to_ui


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(path_to_ui('windows/main.ui'), self)
        self.init_program()

    def init_program(self):
        pass
