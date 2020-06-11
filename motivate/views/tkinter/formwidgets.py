# Standard library imports
import tkinter as tk
import tkinter.messagebox as mb
from pubsub import pub 
# Local application imports
import motivate.currency as currency
from motivate.item import Item
from motivate.views.tkinter.buttonwidgets import Button


class ItemForm(tk.LabelFrame):
    form_fields = 'Category', 'Name', currency.append_currency_symbol('Price')

    def __init__(self, master):
        super().__init__(
            master=master, 
            text='Modify An Item or Create Your Own'
            )
        self.master = master
        # Create widgets             
        labels = [tk.Label(self, text=f) for f in self.form_fields]
        self.entries = [tk.Entry(self) for _ in self.form_fields]
        self.update_button = Button(
            master_widget=self, 
            button_text='Update'
            )
        self.delete_button = Button(
            master_widget=self, 
            button_text='Delete'
            )
        self.save_button = Button(
            master_widget=self, 
            button_text='Save as New'
            )
        # Grid widgets  
        self.form_widgets = list(zip(labels, self.entries))
        for i, (label, entry) in enumerate(self.form_widgets): 
            label.grid(row=i, column=0, padx=10, sticky=tk.W)
            entry.grid(row=i, column=1, padx=10, pady=5) 
        for i, button in enumerate(
                [self.update_button, 
                self.delete_button, 
                self.save_button]
                ):
            button.grid(
                row=len(self.form_widgets) + 1,
                column=i,
                padx=1
                )

    def get_item_details(self):
        details = [entry.get() for entry in self.entries]
        try:
            return Item(*details)
        except ValueError as e:
            mb.showerror("Validation error", str(e), parent=self)

    def display_item_details(self, item):
        values = (item.category, item.name,
                  currency.number_formatter(float(item.price)))
        for entry, value in zip(self.entries, values):
            entry.delete(0, tk.END) # or call clear_entries?
            entry.insert(0, value)
  
    def remove_item_details(self):
        for entry in self.entries:
            entry.delete(0, tk.END)

    def bind_update(self, callback):
        def _callback(event=None):
            item = self.get_item_details()
            if item:
                self.master.update_item(item)
                callback(item)
        self.update_button.bind(_callback)

    def bind_delete(self, callback):
        def _callback(event=None):
            self.remove_item_details()
            self.master.delete_item()
            callback()
        self.delete_button.bind(_callback)

    def bind_save(self, callback):
        def _callback(event=None):
            item = self.get_item_details()
            if item:
                self.master.save_item(item)
                callback(item)
        self.save_button.bind(_callback)
  
    
class EarningsForm(tk.LabelFrame):

    def __init__(self, item_price, master_widget):
        super().__init__(master_widget)
        # Create widgets
        label = tk.Label(master=self, text='Earnings')
        message = tk.Message(
            master=self, 
            text=f'/{currency.currency_formatter(item_price)}',
            width=100
            )
        self.earnings_entry = tk.Entry(self)
        self.start_button = Button(
            master_widget=self, 
            button_text='Start'
            )
        self.pause_button = Button(
            master_widget=self, 
            button_text='Pause'
            )
        self.reset_button = Button(
            master_widget=self, 
            button_text='Reset'
            )
        # Grid widgets                                     
        for i, widget in enumerate([label, self.earnings_entry, message]):
            widget.grid(row=0, column=i, padx=10, pady =5)
        for i, button in enumerate([self.start_button, 
                                    self.pause_button, 
                                    self.reset_button]
                                    ):
            button.grid(row=1, column=i, padx=1)
        
    def update_earnings(self, money):
        self.earnings_entry.delete(0, 'end') #tk.END?
        self.earnings_entry.insert('end', currency.currency_formatter(money))

    def bind_start(self, callback):
        def _callback(event=None):
            self.start_button.config(state=tk.DISABLED)
            self.pause_button.config(state=tk.ACTIVE)
            self.reset_button.config(state=tk.DISABLED)
            callback()
        self.start_button.bind(_callback)
       
    def bind_pause(self, callback):
        def _callback(event=None):
            self.start_button.config(state=tk.ACTIVE)
            self.pause_button.config(state=tk.DISABLED)
            self.reset_button.config(state=tk.ACTIVE)
            callback()
        self.pause_button.bind(_callback)
       
    def bind_reset(self, callback):
        def _callback(event=None):
            self.start_button.config(state=tk.ACTIVE)
            self.pause_button.config(state=tk.DISABLED)
            self.reset_button.config(state=tk.DISABLED)
            callback()
        self.reset_button.bind(_callback)

class SalaryForm(tk.LabelFrame):
    
    def __init__(self, master_widget):
        super().__init__(
            master=master_widget,
            text='Set Your Salary'
            )            
        label = tk.Label(
            master=self, 
            text=currency.append_currency_symbol('Annual Salary')
            )
        self.salary_entry = tk.Entry(master=self)
        for i, widget in enumerate([label, self.salary_entry]):
            widget.grid(row=0, column=i, padx=10)
        
    def get_salary(self):
        # TODO: Check user entry is of appropriate form
        return float(self.salary_entry.get())
        