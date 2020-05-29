import tkinter as tk

class ItemList(tk.LabelFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, text = 'Select an Item')
        self.lb = tk.Listbox(self, height=14, **kwargs)
        scroll = tk.Scrollbar(self, command=self.lb.yview)

        self.lb.config(yscrollcommand=scroll.set)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.lb.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    def insert(self, item, index=tk.END):
        text = f"{item.category}, {item.name}, {item.cost}"
        self.lb.insert(index, text)

    def delete(self, index):
        self.lb.delete(index, index)

    def update(self, item, index):
        self.delete(index)
        self.insert(item, index)

    def bind_double_click(self, callback):
        handler = lambda _: callback(self.lb.curselection()[0])
        self.lb.bind("<Double-Button-1>", handler)