# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
from typing import Optional

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget

from common import g
from common.utils import path_to_ui


class MainWindow(QMainWindow):
    main_layout: QVBoxLayout
    current_screen: Optional[QWidget]

    def __init__(self):
        super().__init__()
        g.window = self
        uic.loadUi(path_to_ui('main'), self)
        self.init()

    def init(self):
        self.current_screen = None

    def goto(self, screen):
        if self.current_screen is not None:
            self.current_screen.deleteLater()

        self.clear_window()
        self.current_screen = screen
        self.main_layout.addWidget(self.current_screen)

    def clear_window(self):
        if self.current_screen is not None:
            self.main_layout.removeWidget(self.current_screen)
