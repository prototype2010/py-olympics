import sqlite3


class Connection:
    DB_PATH = './olympic_history.db'

    def get_cursor(self):
        conn = sqlite3.connect(self.DB_PATH)
        return conn.cursor()

    def drop_all_existing(self):
        conn = sqlite3.connect(self.DB_PATH)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM results;')
        cursor.execute('DELETE FROM athletes;')
        cursor.execute('DELETE FROM games;')
        cursor.execute('DELETE FROM events;')
        cursor.execute('DELETE FROM sports;')
        cursor.execute('DELETE FROM teams;')
        conn.commit()
        conn.close()

    def execute_query(self, statement, parameters):
        conn = sqlite3.connect(self.DB_PATH)
        cursor = conn.cursor()
        cursor.execute(statement, parameters)
        conn.commit()
        conn.close()
        return {'id': cursor.lastrowid}
