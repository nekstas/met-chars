# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
from typing import Optional

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget

from common.utils import path_to_ui


class MainWindow(QMainWindow):
    main_layout: QVBoxLayout
    current_screen: Optional[QWidget]

    def __init__(self):
        super().__init__()
        uic.loadUi(path_to_ui('main.ui'), self)
        self.init()

    def init(self):
        self.current_screen = None

    def goto(self, screen, *args, **kwargs):
        self.clear_window()
        self.current_screen = screen(*args, **kwargs)
        self.main_layout.addWidget(self.current_screen)

    def clear_window(self):
        if self.current_screen is not None:
            self.main_layout.removeWidget(self.current_screen)
