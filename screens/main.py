# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
from PyQt5.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_program()

    def init_program(self):
        self.setGeometry(400, 400, 400, 400)
        self.setWindowTitle('Мой проект =)')
