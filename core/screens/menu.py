# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel

from common import g
from core.screens.game_mode_select import GameModeSelectScreen
from core.screens.players import PlayersScreen
from ui.screens.menu import Ui_GameMenu


class MenuScreen(QWidget, Ui_GameMenu):
    exit_btn: QPushButton
    players_btn: QPushButton
    play_btn: QPushButton
    player_name_label: QLabel

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init()

    def init(self):
        PlayersScreen.find_player(self)
        self.player_name_label.setText(f'Игрок: {g.player_name}')
        self.exit_btn.clicked.connect(self.on_exit)
        self.play_btn.clicked.connect(self.on_play)
        self.players_btn.clicked.connect(self.on_players)

    @staticmethod
    def on_play():
        g.window.goto(GameModeSelectScreen())

    @staticmethod
    def on_players():
        g.window.goto(PlayersScreen())

    @staticmethod
    def on_exit():
        g.app.exit()
