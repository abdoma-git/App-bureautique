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
        self.window_list.title("semestralka")
        self.window_list.configure(padx=15, pady=5)

        self.modal_list_title = tk.Label(self.window_list, text="List of producs", font=("Bahnscrift",14,'bold'))
        self.modal_list_title.grid(row=0,column=0,columnspan=4)

        btn_add = ttk.Button(
            self.window_list, text="Add", command=self.add_item_window, style=self.btn_style)
        btn_add.grid(row=1, column=0, columnspan=4)

        # Table Thead
        thead_data = ['ID', 'name', 'amount', 'price']
        counter = 0
        self.table = ttk.Treeview(columns=("#1", "#2", "#3"), height=10)
        for j in thead_data:
            self.table.grid(row=2, column=counter)
            self.table.heading(f'#{counter}', text=j, anchor=CENTER)
            counter += 1

        self.get()

        self.btn_edit = ttk.Button(
            self.window_list, text="edit", command=self.itm_edit)
        self.btn_edit.grid(row=3, column=0, columnspan=4)
        self.btn_delete = ttk.Button(
            self.window_list, text="delete", command=self.delete_item)
        self.btn_delete.grid(row=4, column=0, columnspan=4)

        self.window_list.mainloop()

    def get(self):
        # Table Tbody
        records = self.table.get_children()
        for element in records:
            self.table.delete(element)

        data = db_class().select()

        for i in data:
            self.table.insert('', 0, text=i[0], values=(i[1], i[2], i[3]))

    def add_item(self):
        self.add(self.product_name.get(), self.amount_item.get(),
                 self.product_price.get())
        self.window_add.destroy()
        self.get()

    def add_item_window(self):
        self.window_add = tk.Toplevel()

        self.window_add.title("add products")
        self.window_add.configure(padx=20, pady=20)

        self.itm_add_label = ttk.Label(self.window_add, text="add product",
                                        font=("Bahnschrift", 14, 'bold'))

        self.itm_add_label.grid(row=0, column=1, columnspan=5)

        self.product_name_label = ttk.Label(self.window_add, text="name", width=20)
        self.product_name_label.grid(row=1, column=1, columnspan=2)
        self.product_name = ttk.Entry(self.window_add, width=40)
        self.product_name.grid(row=1, column=3, columnspan=3)

        self.amount_item_label = ttk.Label(self.window_add, text="amount", width=20)
        self.amount_item_label.grid(row=2, column=1, columnspan=2)
        self.amount_item = ttk.Entry(self.window_add, width=40)
        self.amount_item.grid(row=2, column=3, columnspan=3)

        self.product_price_label = ttk.Label(self.window_add, text="price", width=20)
        self.product_price_label.grid(row=3, column=1, columnspan=2)
        self.product_price = ttk.Entry(self.window_add, width=40)
        self.product_price.grid(row=3, column=3, columnspan=3)

        self.btn_add_product = ttk.Button(self.window_add, text="register product",
                                            command=self.add_item)
        self.btn_add_product.grid(row=4, column=1, columnspan=5)

        self.window_add.mainloop()

    def edit(self):
        cod = self.product_id.get()
        name = self.product_name.get()
        amount = self.amount_item.get()
        price = self.product_price.get()
        self.update(name, amount, price, cod)
        self.window_edit.destroy()
        self.get()

    def itm_edit(self):
        cod = self.table.item(self.table.selection())['text']
        name = self.table.item(self.table.selection())['values'][0]
        amount = self.table.item(self.table.selection())['values'][1]
        price = self.table.item(self.table.selection())['values'][2]

        self.window_edit = tk.Toplevel()
        self.window_edit.title("edit product")
        self.window_edit.configure(padx=20, pady=20)

        self.itm_edit_label = ttk.Label(
            self.window_edit, text="edit products",font=("Bahnschrift", 14, 'bold'))
        self.itm_edit_label.grid(row=0, column=0, columnspan=2)

        self.product_id_label = tk.Label(self.window_edit, text="Id")
        self.product_id_label.grid(row=1, column=0)
        self.product_id = tk.Entry(self.window_edit, textvariable=StringVar(self.window_edit, value=cod),
                                    state='readonly', width=30)
        self.product_id.grid(row=1, column=1)

        self.product_name_label = tk.Label(self.window_edit, text="name")
        self.product_name_label.grid(row=2, column=0)

        self.product_name = tk.Entry(self.window_edit, textvariable=StringVar(self.window_edit, value=name),
                                        width=30)
        self.product_name.grid(row=2, column=1)

        self.amount_item_label = tk.Label(self.window_edit, text="amount")
        self.amount_item_label.grid(row=3, column=0)

        self.amount_item = tk.Entry(self.window_edit, textvariable=StringVar(self.window_edit,
                                        value=amount), width=30)

        self.amount_item.grid(row=3, column=1)

        self.product_price_label = tk.Label(self.window_edit, text="price")
        self.product_price_label.grid(row=4, column=0)

        self.product_price = tk.Entry(self.window_edit, textvariable=StringVar(self.window_edit,
                                        value=price), width=30)
        self.product_price.grid(row=4, column=1)

        self.btn = ttk.Button(self.window_edit, text="update",
                                command=self.edit).grid(row=5, column=0, columnspan=2)
        self.window_edit.mainloop()

    def delete_item(self):
        print(self.table.item(self.table.selection())['text'])
        self.delete(self.table.item(self.table.selection())['text'])
        self.get()


if __name__ == '__main__':
    window = tk.Tk()
    app = Aplicacion(window)
