# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core.app import App
    from core.main_window import MainWindow
    from sqlite3 import Connection

app: App
window: MainWindow
db_conn: Connection
