# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
from typing import Callable, Optional

from PyQt5.QtWidgets import QWidget, QLabel, QPushButton

from ui.objects.game_mode_item import Ui_GameModeItem


class GameModeItem(QWidget, Ui_GameModeItem):
    on_select: Optional[Callable]

    description_label: QLabel
    select_btn: QPushButton

    def __init__(self, title, description, on_select=None):
        super().__init__()
        self.setupUi(self)
        self.init(title, description, on_select)

    def init(self, title, description, on_select):
        self.on_select = on_select

        self.select_btn.setText(title)
        self.description_label.setText(description)
        self.select_btn.clicked.connect(self.on_select_clicked)

    def on_select_clicked(self):
        if self.on_select is not None:
            self.on_select()
