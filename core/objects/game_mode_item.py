# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
from typing import Callable, Optional

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton

from common.utils import path_to_ui


class GameModeItem(QWidget):
    on_select: Optional[Callable]

    description_label: QLabel
    select_btn: QPushButton

    def __init__(self, title, description, on_select=None):
        super().__init__()
        uic.loadUi(path_to_ui('objects/game_mode_item.ui'), self)
        self.init(title, description, on_select)

    def init(self, title, description, on_select):
        self.on_select = on_select

        self.select_btn.setText(title)
        self.description_label.setText(description)
        self.select_btn.clicked.connect(self.on_select_clicked)

    def on_select_clicked(self):
        if self.on_select is not None:
            self.on_select()
