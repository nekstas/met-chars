# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
from __future__ import annotations

from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from core.app import App
    from core.main_window import MainWindow
    from sqlite3 import Connection

app: App
window: MainWindow
db_conn: Connection
player_id: int = -1
player_name: Optional[str] = None
player_rnd: int = 0
