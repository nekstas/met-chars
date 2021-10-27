# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
from core.screens.level_select import LevelSelectScreen


class RandomLevelSelectScreen(LevelSelectScreen):
    def __init__(self):
        super().__init__(
            title='Случайный режим'
        )
