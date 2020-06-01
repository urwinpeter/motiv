import tkinter as tk
import locale

class ItemList(tk.LabelFrame):
    currency_sym = locale.localeconv()["currency_symbol"]
    def __init__(self, master, **kwargs):
        super().__init__(master, text = 'Select An Item')
        self.lb = tk.Listbox(self, height=14, width =30, **kwargs)
        yscroll = tk.Scrollbar(self, command=self.lb.yview)

        self.lb.config(yscrollcommand=yscroll.set)
        
        yscroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.lb.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    def insert(self, item, index=tk.END):
        text = f"{item.category}, {item.name}, {locale.currency(float(item.price))}"
        self.lb.insert(index, text)

    def delete(self, index):
        self.lb.delete(index, index)

    def clear(self):
        self.lb.delete(0, tk.END)

    def update(self, item, index):
        self.delete(index)
        self.insert(item, index)

    def bind_double_click(self, callback):
        handler = lambda _: callback(self.lb.curselection()[0])
        self.lb.bind("<Double-Button-1>", handler)