from connection import *


class db_class(Connection):
    def __init__(self):
        super().__init__()

    def select(self):
        try:
            cur = self.conn().cursor()
            cur.execute("SELECT * FROM match")
            return cur.fetchall()
        except sqlite3.Error as err:
            print(f"{err}")
        finally:
            self.con.close()

    def add(self,*args):
        try:
            con = self.conn()
            cur = con.cursor()
            cur.execute("INSERT INTO match(team1, team2, date_debut, date_fin, status, cote1, cote2, commentaires) VALUES(?,?,?,?,?,?,?,?)",args)
            con.commit()
            return "The match has been sucesfully added"
        except sqlite3.Error as err:
            print(f"{err}")
        finally:
            self.con.close()
    
    def update(self,*args):
        try:
            con = self.conn()
            cur = con.cursor()
            cur.execute("UPDATE match SET team1 = ?, team2 = ?, date_debut = ?, date_fin = ?, status = ?, cote1 = ?, cote2 = ?, commentaires = ? WHERE id = ?",args)
            con.commit()
            return "Le match a été bien modifié"
        except sqlite3.Error as err:
            print(f"{err}")
        finally:
            self.con.close()

    def delete(self,*args):
        try:
            con = self.conn()
            cur = con.cursor()
            cur.execute("DELETE FROM match WHERE id = ?",args)
            con.commit()
            return "Le match a été supprimé avec success"
        except sqlite3.Error as err:
            print(f"{err}")
        finally:
            self.con.close()