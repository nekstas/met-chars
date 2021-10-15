# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

from common.utils import path_to_ui


class MenuScreen(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(path_to_ui('screens/menu.ui'), self)
        self.init()

    def init(self):
        pass
