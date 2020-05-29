import tkinter as tk
from motivate.item import Item

class Form(tk.LabelFrame):
    """Configures the login page widgets"""
    def __init__(self, master, form_fields, button_fields, *args, **kwargs):
        # Initialise the main frame
        super().__init__(master, *args, **kwargs)
        # Create widgets
        self._create_form(form_fields)
        self._create_buttons(button_fields)
        
    def _create_form(self, fields):
        labels = [tk.Label(self, text=f) for f in fields]
        self.entries = [tk.Entry(self) for _ in fields]
        self.widgets = list(zip(labels, self.entries))
        for i, (label, entry) in enumerate(self.widgets): 
            label.grid(row=i, column=0, padx=10, sticky=tk.W)
            entry.grid(row=i, column=1, padx=10, pady=5)

    def _create_buttons(self, fields):
        self.buttons = [tk.Button(self, **f) for f in fields]
        for i, button in enumerate(self.buttons):
            button.grid(row=len(self.widgets)+1, column=i, padx=1)
    
class SalaryForm(Form):
    form_fields = 'Annual Salary, £', # set to locale currency
    button_fields = []

    def __init__(self, master, *args, **kwargs):
        super().__init__(master, self.form_fields, self.button_fields, *args, text = 'Set Your Salary', **kwargs)
        
    def bind_next(self, callback):
        self.buttons[0].config(command=callback)

    def get_details(self):
        return float(self.entries[0].get())
    
class HomeForm(Form):
    form_fields = 'Earnings, £',
    button_fields = {'text':'Start'}, {'text':'Pause'},{'text':'Reset'}
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, self.form_fields, self.button_fields, *args, **kwargs)
        self.text = tk.Message(self, width = 100)
        self.text.grid(row=len(self.widgets)-1, column = 2)

    def update_money(self, money):
        self.entries[0].delete(0,'end')
        self.entries[0].insert('end', str(money))

    def active_buttons(self, count): # Is this a fishy for loop too? should I pass it each button individually? via the assign callbacks?
        combos = {True: (tk.DISABLED, tk.ACTIVE, tk.DISABLED),
                False: (tk.ACTIVE, tk.DISABLED, tk.ACTIVE),
                None: (tk.ACTIVE, tk.DISABLED, tk.DISABLED)}
        for i, button in enumerate(self.buttons):
            button.config(state=combos[count][i])

    def set_target(self, value):
        self.text.config(text = f'/£{value}')

    def bind_start(self, callback):
        self.buttons[0].config(command = callback)
        self.buttons[0].bind('<Return>', callback)
    
    def bind_pause(self, callback):
        self.buttons[1].config(command = callback)
        self.buttons[1].bind('<Return>', callback)

    def bind_reset(self, callback):
        self.buttons[2].config(command = callback)
        self.buttons[2].bind('<Return>', callback)

class ItemForm(Form):
    form_fields = 'Category', 'Name', 'Price, £'
    button_fields = {'text':'Update'}, {'text':'Delete'}, {'text':'Save as New'}
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, self.form_fields, self.button_fields, *args, text = 'Modify An Item or Create Your Own', **kwargs)

    def get_details(self):
        details = [e.get() for e in self.entries]
        try:
            return Item(*details)
        except ValueError as e:
            mb.showerror("Validation error", str(e), parent=self)

    def load_details(self, item):
        values = (item.category, item.name,
                  item.price)
        for entry, value in zip(self.entries, values):
            entry.delete(0, tk.END)
            entry.insert(0, value)
  
    def clear_details(self):
        for entry in self.entries:
            entry.delete(0, tk.END)

    def bind_update(self, callback):
        self.buttons[0].config(command=callback)
        self.buttons[0].bind('<Return>', callback)

    def bind_delete(self, callback):
        self.buttons[1].config(command=callback)
        self.buttons[0].bind('<Return>', callback)

    def bind_save(self, callback):
        self.buttons[2].config(command=callback)
        self.buttons[0].bind('<Return>', callback)

