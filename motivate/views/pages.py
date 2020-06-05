import tkinter as tk
import tkinter.messagebox as mb
from motivate.views.formwidgets import EarningsForm, SalaryForm, ItemForm
from motivate.views.listwidgets import ItemList
from motivate.views.canvaswidgets import PieChart
from motivate.views.buttonwidgets import Button

class LoginPage(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        root.title("Settings")
        root.geometry('800x350')
        self.item_listbox = ItemList(self)
        self.item_form = ItemForm(self)
        self.salary_form = SalaryForm(self)
        self.next_button = Button(self, button_text='Next >')
        self._pack()

    '''def start(self):
        root.mainloop() # This seems a bit hidden away here for an important function'''
    
    def _pack(self):
        self.pack() # Pack Login Page Inside Tk 
        # Pack the remaining widgets inside Login Page
        self.item_listbox.pack(side=tk.LEFT, padx=10, pady=10)
        self.item_form.pack(padx=10, pady=10)
        self.salary_form.pack(pady=10)
        self.next_button.pack(side=tk.BOTTOM, pady=5)
        self.item=None
        self.salary=None
        
    def assign_callbacks(self, control, mastercontrol):
        self.item_listbox.bind_double_click(control.select_item)
        self.item_form.bind_update(control.update_item)
        self.item_form.bind_delete(control.delete_item)
        self.item_form.bind_save(control.create_item)
        self.bind_next(mastercontrol.load_homepage)

    def bind_next(self, callback):
        self.next_button.bind(callback)

    def append_item(self, item):
        self.item_listbox.insert_item(item)

    def update_item(self, item, index):
        self.item_listbox.update_item(item, index)

    def remove_items(self):
        self.item_form.clear_entries()
        self.item_listbox.clear_items()

    def get_item_details(self):
        self.item = self.item_form.get_item_details()
        return self.item

    def display_item_details(self, item):
        self.item_form.display_item_details(item)

    def get_salary(self):
        self.salary = self.salary_form.get_salary()
        return self.salary

    def show(self):
        self.grab_set()
        self.wait_window()
        return self.item, self.salary


class HomePage(tk.Frame):
    def __init__(self, quote, price, root):
        super().__init__(root)
        root.title("Progress")
        self.earnings_form = EarningsForm(
                            item_price=price, 
                            master_widget=self
                            )
        self.quote = tk.Message(
                                master=self, 
                                text = quote, 
                                width=300, 
                                justify =tk.CENTER, 
                                font = ("Helvetica", 16, "bold italic")
                                )
        self.piechart = PieChart(self, price)
        self._pack()
    
    def _pack(self):
        self.pack()
        self.quote.pack()
        self.earnings_form.pack()
        self.piechart.pack()

    def assign_callbacks(self, control, mastercontrol):
        self.earnings_form.bind_start(control.start)
        self.earnings_form.bind_pause(control.pause_money)
        self.earnings_form.bind_reset(control.reset_money)

    def update_earnings(self, money):
        self.earnings_form.update_earnings(money)
        self.piechart.update_chart(money)
        
    def update_status(self, count):
        self.earnings_form.update_button_status(count)

    def display_congrats(self, name):
        mb.showinfo(
                    title='CONGRATULATIONS', 
                    message=f"Enjoy your {name}",
                    parent = self
                    )
        