# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав

class SQL:
    CREATE_TABLE_PLAYERS = '''CREATE TABLE IF NOT EXISTS players (
        player_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        player_nick VARCHAR(64) NOT NULL,
        creation_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL 
    );'''
