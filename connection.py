import sqlite3

class Connection:

    def __init__(self):
        pass
    
    def conn(self):
        try:
            self.con = sqlite3.connect('db2')
            return self.con
        except sqlite3.Error as err:
            print(f"connection failed! {err}")