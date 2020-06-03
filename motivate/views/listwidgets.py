import tkinter as tk
import locale

class ItemList(tk.LabelFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, text = 'Select An Item')
        self.listbox = tk.Listbox(self, height=14, width =30, **kwargs)
        yscroll = tk.Scrollbar(self, command=self.listbox.yview)
        self.listbox.config(yscrollcommand=yscroll.set)
        yscroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    def insert_item(self, item, index=tk.END):
        text = f'{item.category}, {item.name}, {locale.currency(float(item.price))}'
        self.listbox.insert(index, text)

    def delete_item(self, index):
        self.listbox.delete(index, index)

    def clear_items(self):
        self.listbox.delete(0, tk.END)

    def update_item(self, item, index):
        self.delete(index)
        self.insert(item, index)

    def bind_double_click(self, callback):
        self.listbox.bind(
                        "<Double-Button-1>",
                        lambda _: callback(self.listbox.curselection()[0])
                        )