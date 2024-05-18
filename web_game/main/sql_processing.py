import sqlite3


class DatabaseConnection:
    def __init__(self, db_name='Countries.db'):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS 
                Countries_list(OperationID INTEGER PRIMARY 
                KEY AUTOINCREMENT, CountryName TEXT, CapitalCity TEXT, Description TEXT)""")
        self.conn.commit()

    def execute_request(self, request, params=None):
        if params is not None:
            self.cursor.execute(request, params)
            self.conn.commit()
        else:
            self.cursor.execute(request)
            self.conn.commit()
        return self.cursor.fetchall()



    def close_connection(self):
        self.conn.close()


