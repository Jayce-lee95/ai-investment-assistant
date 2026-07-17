import sqlite3
from pathlib import Path

# 数据库文件位置
DB_PATH = Path("data/investment.db")


class Database:

    def __init__(self):
        DB_PATH.parent.mkdir(exist_ok=True)
        self.conn = sqlite3.connect(DB_PATH)
        self.cursor = self.conn.cursor()

    def create_tables(self):
        """创建数据库表"""

        # 基金表
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS funds(
            fund_code TEXT PRIMARY KEY,
            fund_name TEXT,
            platform TEXT,
            current_share REAL DEFAULT 0,
            average_cost REAL DEFAULT 0
        )
        """)

        # 交易记录
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            trade_date TEXT,
            fund_code TEXT,
            direction TEXT,
            amount REAL,
            share REAL,
            cost REAL,
            status TEXT
        )
        """)

        self.conn.commit()

    def close(self):
        self.conn.close()
