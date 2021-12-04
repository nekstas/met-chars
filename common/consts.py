# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
from core.other.cell_b import CellB

PATH_TO_USER_DATA = './user_data'
PATH_TO_PROGRAM_DATA = './data'
DB_FILE = 'db.sqlite'
PLAYER_FILE = 'player.txt'
PLAYER_NAME_MAX_LEN = 30
WORD_MAX_LEN = 30
CELLS_H_COUNT = 4
CELLS_V_COUNT = 5

# Игровое поле, если оно не задано для уровня
BASE_BOARD_CELLS = [
    [0x401 | CellB.ENABLED, 0x401 | CellB.ENABLED, CellB.ENABLED, 0x276 | CellB.ENABLED],
    [CellB.ENABLED, CellB.ENABLED, CellB.ENABLED, 0x289 | CellB.ENABLED],
    [CellB.ENABLED, CellB.ENABLED, CellB.ENABLED, 0x26a | CellB.ENABLED],
    [CellB.ENABLED, CellB.ENABLED, CellB.ENABLED, 0x205 | CellB.ENABLED],
    [0x201 | CellB.ENABLED, 0x202 | CellB.ENABLED, 0x203 | CellB.ENABLED, 0x244 | CellB.ENABLED]
]
