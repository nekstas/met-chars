# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
from core.screens.level_select import LevelSelectScreen


class PlotLevelSelectScreen(LevelSelectScreen):
    def __init__(self):
        super().__init__(
            title='Сюжетный режим'
        )
