import tkinter as tk
import tkinter.messagebox as mb

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
        self.entries = [tk.Entry(self, textvariable = tk.StringVar()) for _ in fields]
        self.widgets = list(zip(labels, self.entries))
        for i, (label, entry) in enumerate(self.widgets): ### CREATE A FUNCTION TO REPLACE THIS REPEATED CODE?
            label.grid(row=i, column=0, padx=10, sticky=tk.W)
            entry.grid(row=i, column=1, padx=10, pady=5)

    def get_details(self):
        details = [e.get() for e in self.entries]
        try:
            return Contact(details)
        except ValueError as e:
            print(str(e))


### Do i need to define a new class here or should I just put SetMoney function in 
### Form classes even though it won't be applicable in some cases
class HomeForm(Form):
    def __init__(self, master, fields):
        super().__init__(master, fields, width = 30)
        
    def SetMoney(self, money):
        self.moneyCtrl.delete(0,'end')
        self.moneyCtrl.insert('end', str(money))       

class EventWidget(tk.Frame):
    def __init__(self, master, fields):
        self.master = master
        self._create_buttons(fields) 
        
    def _create_buttons(self, fields):
        self.buttons = [tk.Button(self.master, **f) for f in fields]
        for i, button in enumerate(self.buttons):
            button.grid(row=len(self.master.widgets)+i, column=1, columnspan=1, padx=10)
            
    def attach(self, observer, commands): # Get rid of this and pass commands in via states
        # commands = [observer.Submit] THIS NEEDS MOVING TO POINT OF CALL
        for i, button in enumerate(self.buttons): ### USe mapping instead
            button.config(command=commands[i])

class HomeEventWidget(EventWidget):
    def __init__(self, master, fields):
        super().__init__(master, fields)

    def SetCount(self, count):
        combos = {True: (tk.DISABLED, tk.ACTIVE, tk.DISABLED),
                False: (tk.ACTIVE, tk.DISABLED, tk.ACTIVE),
                None: (tk.ACTIVE, tk.DISABLED, tk.DISABLED)}
        for i, button in enumerate(self.buttons):
            button.config(state=combos[count][i])