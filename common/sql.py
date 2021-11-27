# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
from common.consts import PLAYER_NAME_MAX_LEN, WORD_MAX_LEN


class SQL:
    # Создание таблиц
    CREATE_TABLE_PLAYERS = f'''CREATE TABLE IF NOT EXISTS players (
        player_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        player_name VARCHAR({PLAYER_NAME_MAX_LEN}) NOT NULL,
        player_rnd INTEGER NOT NULL,
        creation_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL 
    );'''

    CREATE_TABLE_COMPLETED_LEVELS = f'''CREATE TABLE IF NOT EXISTS completed_levels (
        completed_level_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        player_id INTEGER NOT NULL,
        level_word VARCHAR({WORD_MAX_LEN}) NOT NULL,
        level_game_mode CHAR(1) NOT NULL,
        level_num INTEGER NOT NULL,
        best_moves_count INTEGER NOT NULL,
        best_time INTEGER NOT NULL,
        completion_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
        FOREIGN KEY (player_id) REFERENCES players (player_id)
        ON DELETE CASCADE ON UPDATE CASCADE
    );'''

    # Действия с игроками
    CREATE_NEW_PLAYER = '''INSERT INTO 
        players (player_name, player_rnd)
        VALUES (?, ?);'''

    GET_PLAYER_NAME_BY_ID = '''SELECT player_name, player_rnd
        FROM players
        WHERE player_id=?;'''

    GET_PLAYERS = '''SELECT player_id, player_name, player_rnd
        FROM players;'''

    DELETE_PLAYER = '''DELETE FROM players
        WHERE player_id=?;'''

    CHANGE_PLAYER_NAME = '''UPDATE players
        SET player_name=?
        WHERE player_id=?;'''

    CHANGE_PLAYER_RND = '''UPDATE players
        SET player_rnd=?
        WHERE player_id=?;'''

    # Действия с пройденными уровнями
    GET_COMPLETED_PLOT_LEVELS_BY_PLAYER_ID = '''SELECT 
        completed_level_id, level_num, level_word, best_moves_count, best_time
        FROM completed_levels
        WHERE level_game_mode='p' AND player_id=?
        ORDER BY level_num;'''

    GET_COMPLETED_RANDOM_LEVELS_BY_PLAYER_ID = '''SELECT 
        completed_level_id, level_num, level_word, best_moves_count, best_time
        FROM completed_levels
        WHERE level_game_mode='p' AND player_id=?
        ORDER BY level_num;'''
