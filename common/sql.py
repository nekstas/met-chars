# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
from common.consts import PLAYER_NAME_MAX_LEN


class SQL:
    CREATE_TABLE_PLAYERS = f'''CREATE TABLE IF NOT EXISTS players (
        player_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        player_name VARCHAR({PLAYER_NAME_MAX_LEN}) NOT NULL,
        creation_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL 
    );'''

    CREATE_NEW_PLAYER = '''INSERT INTO 
        players (player_name)
        VALUES (?);'''

    GET_PLAYER_NAME_BY_ID = '''SELECT player_name
        FROM players
        WHERE player_id=?;'''

    GET_PLAYERS = '''SELECT player_id, player_name
        FROM players;'''

    DELETE_PLAYER = '''DELETE FROM players
        WHERE player_id=?;'''

    CHANGE_PLAYER_NAME = '''UPDATE players
        SET player_name=?
        WHERE player_id=?;'''
