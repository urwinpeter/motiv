import tkinter as tk
from motivate.views.formwidgets import HomeForm, SalaryForm, ItemForm
from motivate.views.listwidgets import ItemList
from motivate.views.canvaswidgets import Pie

class LoginPage(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        root.title("Settings")
        root.geometry('700x350')
        self.list = ItemList(self)
        self.itemform = ItemForm(self)
        self.salaryform = SalaryForm(self)
        self.next_button = tk.Button(self, text='Next >')
        self._pack()

    def _pack(self):
        self.pack()    
        self.list.pack(side=tk.LEFT, padx=10, pady=10)
        self.itemform.pack(padx=10, pady=10)
        self.salaryform.pack(pady=10)
        self.next_button.pack(side=tk.BOTTOM, pady=5)
        
    def assign_callbacks(self, control):
        self.list.bind_double_click(control.select_item)
        self.itemform.bind_update(control.update_item)
        self.itemform.bind_delete(control.delete_item)
        self.itemform.bind_save(control.create_item)
        ## need to bind itemform.bind_set()
        self.bind_next(control.load_homepage)

    def bind_next(self, callback):
        self.next_button.config(command=callback)
        self.next_button.bind('<Return>', callback)

    def add_item(self, item): # change name to add to list?
        self.list.insert(item)

    def update_item(self, item, index):
        self.list.update(item, index)

    def remove_item(self, index):
        self.itemform.clear()
        self.list.delete(index)

    def get_details(self):
        return self.itemform.get_details()

    def load_details(self, item):
        self.itemform.load_details(item)

    def get_salary(self):
        return self.salaryform.get_details()

class HomePage(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        #root.wm_title("Progress")
        root.title("Progress")
        self.form = HomeForm(self)
        #self.text = tk.message(self)
        self.canvas = Pie(self)
        self._pack()
    
    def _pack(self):
        self.pack()
        #self.text.pack()
        self.form.pack()
        self.canvas.pack()

    def assign_callbacks(self, control):
        self.form.bind_start(control.Start)
        self.form.bind_pause(control.PauseMoney)
        self.form.bind_reset(control.ResetMoney)

    def display_quote(self, quote):
        self.text.config(text = quote)

    def SetMoney(self, money):
        self.form.SetMoney(money)
        self.canvas.SetMoney(money)
        
    def SetCount(self, count):
        self.form.SetCount(count)

    def congrats(self):
        mb.showinfo(self, "congrats")

    def set_target(self, value):
        self.canvas.set_target(value)
        self.form.set_target(value)