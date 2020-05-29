import tkinter as tk
import tkinter.messagebox as mb
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
        self.pack() # Pack Login Page Inside Tk 
        # Pack the remaining widgets inside Login Page
        self.list.pack(side=tk.LEFT, padx=10, pady=10)
        self.itemform.pack(padx=10, pady=10)
        self.salaryform.pack(pady=10)
        self.next_button.pack(side=tk.BOTTOM, pady=5)
        
    def assign_callbacks(self, control):
        self.list.bind_double_click(control.select_item)
        self.itemform.bind_update(control.update_item)
        self.itemform.bind_delete(control.delete_item)
        self.itemform.bind_save(control.create_item)
        self.bind_next(control.load_homepage)

    def bind_next(self, callback):
        self.next_button.config(command=callback)
        self.next_button.bind('<Return>', callback)

    def add_item(self, item):
        self.list.insert(item)

    def update_item(self, item, index):
        self.list.update(item, index)

    def remove_items(self):
        self.itemform.clear_details()
        self.list.clear()

    def get_details(self): # change to get_item_details?
        return self.itemform.get_details()

    def load_details(self, item):
        self.itemform.load_details(item)

    def get_salary(self):
        return self.salaryform.get_details()

class HomePage(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        # root.wm_title("Progress")
        root.title("Progress")
        self.form = HomeForm(self)
        self.quote = tk.Message(self, width=300, justify =tk.CENTER, font = ("Helvetica", 16, "bold italic"))
        self.canvas = Pie(self)
        self._pack()
    
    def _pack(self):
        self.pack()
        self.quote.pack()
        self.form.pack()
        self.canvas.pack()

    def assign_callbacks(self, control):
        self.form.bind_start(control.Start)
        self.form.bind_pause(control.PauseMoney)
        self.form.bind_reset(control.ResetMoney)

    def set_target(self, value):
        self.canvas.set_target(value)
        self.form.set_target(value)

    def update_money(self, money):
        self.form.update_money(money)
        self.canvas.update_chart(money)
        
    def update_count(self, count):
        self.form.active_buttons(count)

    def display_congrats(self, item):
        mb.showinfo(self, f"congrats, {item.name}")

    def display_quote(self, quote):
        self.quote.config(text = quote)