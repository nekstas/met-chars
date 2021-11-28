# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
from common import g
from common.sql import SQL
from core.data.plot_words_list import PlotWordsList
from core.screens.game import GameScreen
from core.screens.level_select import LevelSelectScreen


class PlotLevelSelectScreen(LevelSelectScreen):
    def __init__(self):
        super().__init__(
            title='Сюжетный режим', game_mode='p'
        )

    def on_continue(self):
        # TODO: продумать ситуацию, когда уровни закончились
        g.window.goto(GameScreen(PlotWordsList(), self.max_level + 1))

    def on_new_game(self):
        self.delete_completed_levels()
        g.window.goto(GameScreen(PlotWordsList(), 1))
