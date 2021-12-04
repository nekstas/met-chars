# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
from typing import Optional

from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget

from common import g
from ui.main import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    main_layout: QVBoxLayout
    current_screen: Optional[QWidget]
    current_p: int

    def __init__(self):
        super().__init__()
        g.window = self
        self.setupUi(self)
        self.init()

    def init(self):
        self.current_screen = None
        self.current_p = -1

    def goto(self, screen, p=1, anyway=False):
        if p < self.current_p and not anyway:
            return
        if self.current_screen is not None:
            self.current_screen.deleteLater()

        self.clear_window()
        self.current_screen = screen
        self.current_p = p
        self.main_layout.addWidget(self.current_screen)

    def clear_window(self):
        if self.current_screen is not None:
            self.main_layout.removeWidget(self.current_screen)
