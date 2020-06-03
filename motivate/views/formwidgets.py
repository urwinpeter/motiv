import locale
import tkinter as tk
import tkinter.messagebox as mb
from motivate.item import Item
from motivate.views.buttonwidgets import Button

locale.setlocale(locale.LC_ALL, '')
csymb = locale.localeconv()["currency_symbol"]

class Form(tk.LabelFrame):
    """Configures the login page widgets"""
    def __init__(self, master, form_fields, *args, **kwargs):
        # Initialise the main frame
        super().__init__(master, *args, **kwargs)
        # Create widgets
        self._create_form(form_fields)
        
    def _create_form(self, fields):
        labels = [tk.Label(self, text=f) for f in fields]
        self.entries = [tk.Entry(self) for _ in fields]
        self.widgets = list(zip(labels, self.entries))
        for i, (label, entry) in enumerate(self.widgets): 
            label.grid(row=i, column=0, padx=10, sticky=tk.W)
            entry.grid(row=i, column=1, padx=10, pady=5)
    

class HomeForm(Form):
    form_fields = 'Earnings',
    def __init__(self, master, price, *args, **kwargs):
        super().__init__(master, self.form_fields, *args, **kwargs)
        self.text = tk.Message(self, text = f'/{locale.currency(price)}', width = 100)
        self.text.grid(row=len(self.widgets)-1, column = 2)
        self._create_buttons()

    def _create_buttons(self):
        button_row = len(self.widgets) + 1
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

        self.start_button.grid(row=button_row, column=0, padx=1)
        self.pause_button.grid(row=button_row, column=1, padx=1)
        self.reset_button.grid(row=button_row, column=2, padx=1)

    def update_money(self, money):
        self.entries[0].delete(0,'end') #tk.END?
        self.entries[0].insert('end', str(locale.currency(money))) # Do i need the str?

    def active_buttons(self, count): # Is this a fishy for loop too? should I pass it each button individually? via the assign callbacks?
        return
        combos = {True: (tk.DISABLED, tk.ACTIVE, tk.DISABLED),
                False: (tk.ACTIVE, tk.DISABLED, tk.ACTIVE),
                None: (tk.ACTIVE, tk.DISABLED, tk.DISABLED)}
        for i, button in enumerate(self.buttons):
            button.config(state=combos[count][i])

    def bind_start(self, callback):
        self.start_button.bind(callback)
       
    def bind_pause(self, callback):
        self.pause_button.bind(callback)
       
    def bind_reset(self, callback):
        self.reset_button.bind(callback)

    '''def _bind(self, button, callback):
        button.config(command=callback)
        button.bind('<Return>', callback)'''


class ItemForm(Form):
    form_fields = 'Category', 'Name', f'Price, {csymb}'
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, self.form_fields, *args, text = 'Modify An Item or Create Your Own', **kwargs)
        self._create_buttons()
    
    def _create_buttons(self):
        button_row = len(self.widgets) + 1
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

        self.update_button.grid(row=button_row, column=0, padx=1)
        self.delete_button.grid(row=button_row, column=1, padx=1)
        self.save_button.grid(row=button_row, column=2, padx=1)

    def get_details(self):
        details = [e.get() for e in self.entries]
        try:
            return Item(*details)
        except ValueError as e:
            mb.showerror("Validation error", str(e), parent=self)

    def load_details(self, item):
        values = (item.category, item.name,
                  locale.currency(float(item.price))[1:]) # change to string. remove
        for entry, value in zip(self.entries, values):
            entry.delete(0, tk.END)
            entry.insert(0, value)
  
    def clear_details(self):
        for entry in self.entries:
            entry.delete(0, tk.END)

    def bind_update(self, callback):
        self.update_button.bind(callback)

    def bind_delete(self, callback):
        self.delete_button.bind(callback)

    def bind_save(self, callback):
        self.save_button.bind(callback)

class SalaryForm(Form):
    form_fields = f'Annual Salary, {csymb}', 
    button_fields = []

    def __init__(self, master, *args, **kwargs):
        super().__init__(master, self.form_fields, self.button_fields, *args, text = 'Set Your Salary', **kwargs)
        
    def get_details(self):
        return float(self.entries[0].get())
        