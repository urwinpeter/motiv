# Standard library imports
import tkinter as tk
# Local application imports
import motivate.currency as currency

class ItemList(tk.LabelFrame):
    def __init__(self, master, items):
        super().__init__(master, text = 'Select An Item')
        self.master = master
        self.listbox = tk.Listbox(self, height=14, width =30)
        yscroll = tk.Scrollbar(self, command=self.listbox.yview)
        self.listbox.config(yscrollcommand=yscroll.set)
        yscroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        # TODO: Add xscroll
        for item in items:
            self.insert_item(item)
        self.selection = None

    def insert_item(self, item, index=tk.END):
        text = f'{item.category}, {item.name}, {currency.currency_formatter(float(item.price))}'
        self.listbox.insert(index, text)

    def delete_item(self):
        if self.selection:
            self.listbox.delete(self.selection, self.selection)

    def update_item(self, item):
        self.delete_item()
        self.insert_item(item, self.selection)

    def bind_double_click(self, callback):
        def _callback(event=None):
            self.selection = self.listbox.curselection()[0]
            callback(self.selection)
        self.listbox.bind("<Double-Button-1>", _callback)
            
