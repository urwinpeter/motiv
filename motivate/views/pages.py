import tkinter as tk
import tkinter.messagebox as mb
from motivate.views.formwidgets import HomeForm, SalaryForm, ItemForm
from motivate.views.listwidgets import ItemList
from motivate.views.canvaswidgets import Pie
from motivate.views.buttonwidgets import Button

root = tk.Tk()

class LoginPage(tk.Frame):
    def __init__(self):
        super().__init__(root)
        root.title("Settings")
        root.geometry('800x350')
        self.list = ItemList(self)
        self.itemform = ItemForm(self)
        self.salaryform = SalaryForm(self)
        self.next_button = Button(self, button_text='Next >')
        self._pack()

    def start(self):
        root.mainloop() # This seems a bit hidden away here for an important function
    
    def _pack(self):
        self.pack() # Pack Login Page Inside Tk 
        # Pack the remaining widgets inside Login Page
        self.list.pack(side=tk.LEFT, padx=10, pady=10)
        self.itemform.pack(padx=10, pady=10)
        self.salaryform.pack(pady=10)
        self.next_button.pack(side=tk.BOTTOM, pady=5)
        
    def assign_callbacks(self, control, mastercontrol):
        self.list.bind_double_click(control.select_item)
        self.itemform.bind_update(control.update_item)
        self.itemform.bind_delete(control.delete_item)
        self.itemform.bind_save(control.create_item)
        self.bind_next(mastercontrol.load_homepage)

    def bind_next(self, callback):
        self.next_button.bind(callback)
        #self.next_button.config(command=callback)
        #self.next_button.bind('<Return>', callback)

    def append_item(self, item):
        self.list.insert(item)

    def update_item(self, item, index):
        self.list.update(item, index)

    def remove_items(self):
        self.itemform.clear_details()
        self.list.clear()

    def get_item_details(self):
        return self.itemform.get_details()

    def display_item_details(self, item):
        self.itemform.display_item_details(item)

    def get_salary(self):
        return self.salaryform.get_details()

class HomePage(tk.Frame):
    def __init__(self, quote, price):
        super().__init__(root)
        # root.wm_title("Progress")
        root.title("Progress")
        self.root = root
        self.form = HomeForm(self, price)
        self.quote = tk.Message(self, text = quote, width=300, justify =tk.CENTER, font = ("Helvetica", 16, "bold italic"))
        self.canvas = Pie(self, price)
        self._pack()
    
    def _pack(self):
        self.pack()
        self.quote.pack()
        self.form.pack()
        self.canvas.pack()

    def assign_callbacks(self, control, mastercontrol):
        self.form.bind_start(control.start)
        self.form.bind_pause(control.pause_money)
        self.form.bind_reset(control.reset_money)

    def update_earnings(self, money):
        self.form.update_earnings(money)
        self.canvas.update_chart(money)
        
    def update_status(self, count):
        self.form.update_button_status(count)

    def display_congrats(self, name):
        mb.showinfo('CONGRATULATIONS', f"Enjoy your {name}", parent = self)
        