import sqlite3


class Database:
    def __init__(self, db_name='IVN_DB.db'):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()

    def execute(self, query, params=()):
        self.cur.execute(query, params)
        self.conn.commit()
        return self.cur

    def fetchall(self):
        return self.cur.fetchall()

    def fetchone(self):
        return self.cur.fetchone()

    def close(self):
        self.conn.close()
