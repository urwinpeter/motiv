import tkinter as tk
import tkinter.messagebox as mb
from motivate.contact import Contact

class Form(tk.Frame):
    """Configures the login page widgets"""
    def __init__(self, master, fields, *args, **kwargs):
        # Initialise the main frame
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.pack()
        # Create widgets
        self._create_form(fields)
        
    def _create_form(self, fields):
        labels = [tk.Label(self, text=f) for f in fields]
        self.entries = [tk.Entry(self) for _ in fields]
        self.widgets = list(zip(labels, self.entries))
        for i, (label, entry) in enumerate(self.widgets): ### CREATE A FUNCTION TO REPLACE THIS REPEATED CODE?
            label.grid(row=i, column=0, padx=10, sticky=tk.W)
            entry.grid(row=i, column=1, padx=10, pady=5)

    def get_details(self):
        details = [e.get() for e in self.entries]
        try:
            return Contact(*details)
        except ValueError as e:
            mb.showerror("Validation error", str(e), parent=self)

    def error(self, message):
        mb.showerror("Error", message, parent=self)

class HomeForm(Form):
    def __init__(self, master, fields):
        super().__init__(master, fields, width = 30)
        
    def SetMoney(self, money):
        self.entries[0].delete(0,'end')
        self.entries[0].insert('end', str(money))
    
class EventWidget(tk.Frame):
    def __init__(self, master, fields):
        self.master = master
        self._create_buttons(fields) 
        
    def _create_buttons(self, fields):
        self.buttons = [tk.Button(self.master, **f) for f in fields]
        for i, button in enumerate(self.buttons):
            button.grid(row=len(self.master.widgets)+i, column=1, columnspan=1, padx=10)
            
class RegisterEventWidget(EventWidget):
    def __init__(self, master, fields):
        super().__init__(master, fields)
     
    def set_ctrl(self, observer):
        commands = observer.Submit, observer.Register
        for i, button in enumerate(self.buttons): 
            button.config(command=commands[i])
            button.bind("<Return>", commands[i])

class LoginEventWidget(EventWidget):
    def __init__(self, master, fields):
        super().__init__(master, fields) 
        
    def set_ctrl(self, observer):
        commands = observer.Submit, observer.Register
        for i, button in enumerate(self.buttons): 
            button.config(command=commands[i])
            button.bind("<Return>", commands[i])

class HomeEventWidget(EventWidget):
    def __init__(self, master, fields):
        super().__init__(master, fields) 
        
    def set_ctrl(self, observer):
        commands = observer.Start, observer.PauseMoney, observer.ResetMoney
        for i, button in enumerate(self.buttons):
            button.config(command=commands[i])
            button.bind("<Return>", commands[i])

    def SetCount(self, count):
        combos = {True: (tk.DISABLED, tk.ACTIVE, tk.DISABLED),
                False: (tk.ACTIVE, tk.DISABLED, tk.ACTIVE),
                None: (tk.ACTIVE, tk.DISABLED, tk.DISABLED)}
        for i, button in enumerate(self.buttons):
            button.config(state=combos[count][i])
