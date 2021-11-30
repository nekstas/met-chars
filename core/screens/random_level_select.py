# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
import random

from common import g
from common.sql import SQL
from core.data.random_words_list import RandomWordsList
from core.screens.game import GameScreen
from core.screens.level_select import LevelSelectScreen


class RandomLevelSelectScreen(LevelSelectScreen):
    def __init__(self):
        super().__init__(
            title='Случайный режим',
            game_mode='r'
        )

    @staticmethod
    def regen_player_rnd():
        g.player_rnd = random.randint(1, 10 ** 9)
        cur = g.db_conn.cursor()
        cur.execute(SQL.CHANGE_PLAYER_RND, (g.player_rnd, g.player_id))
        g.db_conn.commit()

    def on_continue(self):
        g.window.goto(GameScreen(RandomWordsList(), self.max_level + 1))

    def on_new_game(self):
        self.delete_completed_levels()
        self.regen_player_rnd()
        g.window.goto(GameScreen(RandomWordsList(), 1))
