# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
from common import g
from common.sql import SQL
from core.screens.game import GameScreen
from core.screens.level_select import LevelSelectScreen


class RandomLevelSelectScreen(LevelSelectScreen):
    def __init__(self):
        super().__init__(
            title='Случайный режим',
            get_levels_sql=SQL.GET_COMPLETED_PLOT_LEVELS_BY_PLAYER_ID
        )

    def on_new_game(self):
        g.window.goto(GameScreen())
