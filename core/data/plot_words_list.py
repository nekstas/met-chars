# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
from common.utils import path_to_program_data
from core.data.words_list import WordsList


class PlotWordsList(WordsList):
    def __init__(self):
        super().__init__(path_to_program_data('words/plot.txt'))
