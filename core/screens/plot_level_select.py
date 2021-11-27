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
            title='Сюжетный режим',
            get_levels_sql=SQL.GET_COMPLETED_PLOT_LEVELS_BY_PLAYER_ID
        )

    def on_new_game(self):
        g.window.goto(GameScreen(PlotWordsList(), 1))
