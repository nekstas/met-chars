# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав


class WordsList:
    def __init__(self, words_path):
        self.words = []
        self.load_words(words_path)

    def load_words(self, words_path):
        with open(words_path, 'r', encoding='UTF-8') as words_file:
            self.words = [*map(str.strip, words_file.readlines())]

    def get_word(self, i):
        return self.words[i].lower()
