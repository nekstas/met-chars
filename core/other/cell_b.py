# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав


class CellB:
    ACTION_CHARS = ' +-*/ECRUN'

    DATA, IS_ENABLED, TYPE = 0xFF, 0x100, 0xE00

    L1, L1_SHIFT = 0xF0, 4
    L2, L2_SHIFT = 0xF, 0

    DISABLED, ENABLED = 0, 0x100

    FREE, ACTION, NUMBER, CHAR_RU, CHAR_EN = 0, 0x200, 0x400, 0x600, 0x800
