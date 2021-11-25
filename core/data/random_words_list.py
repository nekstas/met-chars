# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
import random

from common import g
from common.utils import path_to_program_data
from core.data.words_list import WordsList


class RandomWordsList(WordsList):
    def __init__(self):
        super().__init__(path_to_program_data('words/random.txt'))
        self.last_player_id = -1

    def shuffle(self):
        rand = random.Random()
        rand.seed(g.player_id)
        rand.shuffle(self.words)

    def get_word(self, i):
        if g.player_id != self.last_player_id:
            self.shuffle()
            self.last_player_id = g.player_id
        return super().get_word(i)
