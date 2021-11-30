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

    CREATE_TABLE_LEVEL_STATISTICS = f'''CREATE TABLE IF NOT EXISTS level_statistics (
        level_statistics_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        player_id INTEGER NOT NULL,
        level_word VARCHAR({WORD_MAX_LEN}) NOT NULL,
        level_game_mode CHAR(1) NOT NULL,
        moves_count INTEGER NOT NULL,
        time_seconds INTEGER NOT NULL,
        creation_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
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
    GET_COMPLETED_LEVELS = '''SELECT 
            level_num, level_word, best_moves_count, best_time
        FROM completed_levels
        WHERE player_id=? AND level_game_mode=?
        ORDER BY level_num;'''

    ADD_COMPLETED_LEVEL = '''INSERT INTO 
        completed_levels(
            player_id, level_word, level_game_mode, level_num, 
            best_moves_count, best_time
        )
        VALUES(?, ?, ?, ?, ?, ?);'''

    UPDATE_COMPLETED_LEVEL = '''UPDATE completed_levels
        SET 
            best_moves_count=MIN(best_moves_count, ?),
            best_time=MIN(best_time, ?)
        WHERE
            player_id=? AND level_num=? AND level_game_mode=?;'''

    CHECK_COMPLETED_LEVEL = '''SELECT 1
        FROM completed_levels
        WHERE player_id=? AND level_num=? AND level_game_mode=?;'''

    DELETE_COMPLETED_LEVELS = '''DELETE FROM completed_levels
        WHERE player_id=? AND level_game_mode=?;'''

    # Действия со статистикой
    ADD_LEVEL_STATISTICS = '''INSERT INTO 
        level_statistics(
            player_id, level_word, level_game_mode, 
            moves_count, time_seconds
        )
        VALUES(?, ?, ?, ?, ?);'''
