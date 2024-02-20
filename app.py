from tkinter import StringVar, font, ttk
from tkinter.constants import CENTER, W, E, N, S
from d_class import db_class
import tkinter as tk


class Aplicacion(db_class):
    def __init__(self, window):
        super().__init__()
        # Here start the GUI
        self.window = window

        self.btn_style = ttk.Style().configure("TButton", padding=6, font=("Bahnschrift", 12, 'bold'))


        self.main_window()

    def main_window(self):

        self.window.destroy() # split windows

        self.window_list = tk.Tk()
        self.window_list.title("STANIA-Administrateur")
        self.window_list.configure(padx=1, pady=20)
        self.window_list.geometry("1500x1000")

        self.modal_list_title = tk.Label(self.window_list, text="Liste des matchs", font=("Bahnscrift",14,'bold'))
        self.modal_list_title.grid(row=0,column=0,columnspan=4)

        btn_add = ttk.Button(
            self.window_list, text="Add", command=self.add_item_window, style=self.btn_style)
        btn_add.grid(row=1, column=0, columnspan=4)

        # Table Thead
        thead_data = ['ID', 'team1', 'team2', 'date_debut', 'date_fin', 'status', 'cote1', 'cote2', 'Commentaire']
        counter = 0
        self.table = ttk.Treeview(columns=("#1", "#2", "#3", "#4", "#5", "#6", "#7", "#8", "#9" ), height=10)
        for j in thead_data:
            self.table.grid(row=2, column=counter)
            self.table.heading(f'#{counter}', text=j, anchor=CENTER)
            counter += 1

        self.get()

        self.btn_edit = ttk.Button(
            self.window_list, text="edit", command=self.itm_edit)
        self.btn_edit.grid(row=3, column=3, columnspan=4)
        self.btn_delete = ttk.Button(
            self.window_list, text="delete", command=self.delete_item)
        self.btn_delete.grid(row=4, column=3, columnspan=4)

        self.window_list.mainloop()

    def get(self):
        # Table Tbody
        records = self.table.get_children()
        for element in records:
            self.table.delete(element)

        data = db_class().select()

        for i in data:
            self.table.insert('', 0, text=i[0], values=(i[1], i[2], i[3], i[4], i[5], i[6], i[7]))

    def add_item(self):
        self.add(
                self.team1_name.get(),
                self.team2_name.get(),
                self.date_debut.get(),
                self.date_fin.get(),
                self.status.get(),
                self.cote1.get(),
                self.cote2.get(),
                self.commentaire.get(),
        )

        self.window_add.destroy()
        self.get()

    def add_item_window(self):
        self.window_add = tk.Toplevel()

        self.window_add.title("Ajouter un Match")
        self.window_add.configure(padx=20, pady=20)

        self.itm_add_label = ttk.Label(self.window_add, text="Ajouter match",
                                        font=("Bahnschrift", 14, 'bold'))

        self.itm_add_label.grid(row=0, column=1, columnspan=5)

        self.team1_name_label = ttk.Label(self.window_add, text="Team 1", width=20)
        self.team1_name_label.grid(row=1, column=1, columnspan=2)
        self.team1_name = ttk.Entry(self.window_add, width=40)
        self.team1_name.grid(row=1, column=3, columnspan=3)

        self.team2_name_label = ttk.Label(self.window_add, text="Team 2", width=20)
        self.team2_name_label.grid(row=2, column=1, columnspan=2)
        self.team2_name = ttk.Entry(self.window_add, width=40)
        self.team2_name.grid(row=2, column=3, columnspan=3)

        self.date_debut_label = ttk.Label(self.window_add, text="Date de début", width=20)
        self.date_debut_label.grid(row=3, column=1, columnspan=2)
        self.date_debut = ttk.Entry(self.window_add, width=40)
        self.date_debut.grid(row=3, column=3, columnspan=3)

        self.date_fin_label = ttk.Label(self.window_add, text="Date de fin", width=20)
        self.date_fin_label.grid(row=4, column=1, columnspan=2)
        self.date_fin = ttk.Entry(self.window_add, width=40)
        self.date_fin.grid(row=4, column=3, columnspan=3)

        self.status_label = ttk.Label(self.window_add, text="status", width=20)
        self.status_label.grid(row=5, column=1, columnspan=2)
        self.status = ttk.Entry(self.window_add, width=40)
        self.status.grid(row=5, column=3, columnspan=3)

        self.cote1_label = ttk.Label(self.window_add, text="La cote de l'équipe 1", width=20)
        self.cote1_label.grid(row=5, column=1, columnspan=2)
        self.cote1 = ttk.Entry(self.window_add, width=40)
        self.cote1.grid(row=5, column=3, columnspan=3)

        self.cote2_label = ttk.Label(self.window_add, text="La cote de l'équipe 2", width=20)
        self.cote2_label.grid(row=6, column=1, columnspan=2)
        self.cote2 = ttk.Entry(self.window_add, width=40)
        self.cote2.grid(row=6, column=3, columnspan=3)

        self.commentaire_label = ttk.Label(self.window_add, text="Commentaires", width=20)
        self.commentaire_label.grid(row=7, column=1, columnspan=2)
        self.commentaire = ttk.Entry(self.window_add, width=40)
        self.commentaire.grid(row=7, column=3, columnspan=3)



        self.btn_add_product = ttk.Button(self.window_add, text="Ajouter le match",
                                            command=self.add_item)
        self.btn_add_product.grid(row=8, column=1, columnspan=5)

        self.window_add.mainloop()

    def edit(self):
        cod = self.match_id.get()
        team1 = self.team1_name.get()
        team2 = self.team2_name.get()
        date_debut = self.date_debut.get()
        date_fin = self.date_fin.get()
        status = self.status.get()
        cote1 = self.cote1.get()
        cote2 = self.cote2.get()
        commentaire = self.commentaire.get()

        self.update(team1, team2, date_debut, date_fin, status, cote1, cote2, commentaire, cod)

        self.window_edit.destroy()
        self.get()

    def itm_edit(self):
        cod = self.table.item(self.table.selection())['text']
        team1 = self.table.item(self.table.selection())['values'][0]
        team2 = self.table.item(self.table.selection())['values'][1]
        date_debut = self.table.item(self.table.selection())['values'][2]
        date_fin = self.table.item(self.table.selection())['values'][3]
        status = self.table.item(self.table.selection())['values'][4]
        cote1 = self.table.item(self.table.selection())['values'][5]
        cote2 = self.table.item(self.table.selection())['values'][6]
        commentaire = self.table.item(self.table.selection())['values'][6]

        self.window_edit = tk.Toplevel()
        self.window_edit.title("edit product")
        self.window_edit.configure(padx=20, pady=20)

        self.itm_edit_label = ttk.Label(self.window_edit, text="Modifier match",font=("Bahnschrift", 14, 'bold'))
        self.itm_edit_label.grid(row=0, column=0, columnspan=2)

        self.match_id_label = tk.Label(self.window_edit, text="Id")
        self.match_id_label.grid(row=1, column=0)
        self.match_id = tk.Entry(self.window_edit, textvariable=StringVar(self.window_edit, value=cod), state='readonly', width=30)
        self.match_id.grid(row=1, column=1)

        self.team1_name_label = tk.Label(self.window_edit, text="Team 1")
        self.team1_name_label.grid(row=2, column=0)
        self.team1_name = tk.Entry(self.window_edit, textvariable=StringVar(self.window_edit, value=team1), width=30)
        self.team1_name.grid(row=2, column=1)

        self.team2_name_label = tk.Label(self.window_edit, text="Team 2")
        self.team2_name_label.grid(row=3, column=0)
        self.team2_name = tk.Entry(self.window_edit, textvariable=StringVar(self.window_edit, value=team2), width=30)
        self.team2_name.grid(row=3, column=1)

        self.date_debut_label = tk.Label(self.window_edit, text="Date de début")
        self.date_debut_label.grid(row=4, column=0)
        self.date_debut = tk.Entry(self.window_edit, textvariable=StringVar(self.window_edit, value=date_debut), width=30)
        self.date_debut.grid(row=4, column=1)

        self.date_fin_label = tk.Label(self.window_edit, text="Date de fin")
        self.date_fin_label.grid(row=5, column=0)
        self.date_fin = tk.Entry(self.window_edit, textvariable=StringVar(self.window_edit, value=date_fin),width=30)
        self.date_fin.grid(row=5, column=1)

        self.status_label = tk.Label(self.window_edit, text="status du match")
        self.status_label.grid(row=6, column=0)
        self.status = tk.Entry(self.window_edit, textvariable=StringVar(self.window_edit, value=status), width=30)
        self.status.grid(row=6, column=1)

        self.cote1_label = tk.Label(self.window_edit, text="Cote 1 du match")
        self.cote1_label.grid(row=7, column=0)
        self.cote1 = tk.Entry(self.window_edit, textvariable=StringVar(self.window_edit, value=cote1), width=30)
        self.cote1.grid(row=7, column=1)

        self.cote2_label = tk.Label(self.window_edit, text="Cote 2 du match")
        self.cote2_label.grid(row=8, column=0)
        self.cote2 = tk.Entry(self.window_edit, textvariable=StringVar(self.window_edit, value=cote2), width=30)
        self.cote2.grid(row=8, column=1)

        self.commentaire_label = tk.Label(self.window_edit, text="Commentaire")
        self.commentaire_label.grid(row=9, column=0)
        self.commentaire = tk.Entry(self.window_edit, textvariable=StringVar(self.window_edit, value=commentaire), width=30)
        self.commentaire.grid(row=9, column=1)

        self.btn = ttk.Button(self.window_edit, text="Modifier", command=self.edit).grid(row=10, column=0, columnspan=2)
        self.window_edit.mainloop()

    def delete_item(self):
        print(self.table.item(self.table.selection())['text'])
        self.delete(self.table.item(self.table.selection())['text'])
        self.get()


if __name__ == '__main__':
    window = tk.Tk()
    app = Aplicacion(window)
