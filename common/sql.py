# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
from common.consts import PLAYER_NAME_MAX_LEN


class SQL:
    CREATE_TABLE_PLAYERS = f'''CREATE TABLE IF NOT EXISTS players (
        player_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        player_name VARCHAR({PLAYER_NAME_MAX_LEN}) NOT NULL,
        creation_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL 
    );'''

    CREATE_NEW_PLAYER = f'''INSERT INTO 
        players (player_name)
        VALUES (?);'''

    GET_PLAYER_NAME_BY_ID = f'''SELECT player_name
        FROM players
        WHERE player_id=?;'''
