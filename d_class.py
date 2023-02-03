from connection import *

class db_class(Connection):
    def __init__(self):
        super().__init__()

    def select(self):
        try:
            cur = self.conn().cursor()
            cur.execute("SELECT * FROM sem")
            return cur.fetchall()
        except sqlite3.Error as err:
            print(f"{err}")
        finally:
            self.con.close()

    def add(self,*args):
        try:
            con = self.conn()
            cur = con.cursor()
            cur.execute("INSERT INTO sem(name, amount, price) VALUES(?,?,?)",args)
            con.commit()
            return "product has been sucesfully added"
        except sqlite3.Error as err:
            print(f"{err}")
        finally:
            self.con.close()
    
    def update(self,*args):
        try:
            con = self.conn()
            cur = con.cursor()
            cur.execute("UPDATE sem SET name = ?, amount = ?, price = ? WHERE id = ?",args)
            con.commit()
            return "product has been succesfully edited"
        except sqlite3.Error as err:
            print(f"{err}")
        finally:
            self.con.close()

    def delete(self,*args):
        try:
            con = self.conn()
            cur = con.cursor()
            cur.execute("DELETE FROM sem WHERE id = ?",args)
            con.commit()
            return "product has been deleted"
        except sqlite3.Error as err:
            print(f"{err}")
        finally:
            self.con.close()