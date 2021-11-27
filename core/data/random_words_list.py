# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
import random

from common import g
from common.utils import path_to_program_data
from core.data.words_list import WordsList


class RandomWordsList(WordsList):
    def __init__(self):
        super().__init__(path_to_program_data('words/random.txt'))
        self.last_player_rnd = 0

    def shuffle(self):
        self.words.sort()
        rand = random.Random()
        rand.seed(g.player_rnd)
        rand.shuffle(self.words)

    def get_word(self, i):
        if g.player_rnd != self.last_player_rnd:
            self.shuffle()
            self.last_player_rnd = g.player_rnd
        return super().get_word(i)
