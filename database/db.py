import sqlite3
import os
from datetime import datetime

DB_PATH = "database/phishing.db"


def init_db():
    os.makedirs("database", exist_ok=True)
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT,
                prediction TEXT,
                timestamp TEXT
            )
        ''')


def save_result(email, prediction):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "INSERT INTO results (email, prediction, timestamp) VALUES (?, ?, ?)",
            (email, prediction, datetime.now().isoformat())
        )
