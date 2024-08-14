import sqlite3

class DatabaseManager:
    def __init__(self, db_path='bi_extraction.db'):
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS extracted_data (
            id INTEGER PRIMARY KEY,
            document TEXT,
            data TEXT
        )
        '''
        self.conn.execute(query)
        self.conn.commit()

    def save_extraction(self, document, data):
        query = "INSERT INTO extracted_data (document, data) VALUES (?, ?)"
        self.conn.execute(query, (document, data))
        self.conn.commit()

    def query_data(self, query):
        cursor = self.conn.execute(query)
        return cursor.fetchall()
