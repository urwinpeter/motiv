import tkinter as tk
from motivate.controllers.home import Controller
import tkinter.messagebox as mb
from motivate.contact import Contact

class Login(tk.Frame):
    """Configures the login page widgets"""
    def __init__(self, parent, *args, **kwargs):
        # Initialise the main frame
        super().__init__(parent, *args, **kwargs)
        self.master = parent
        self.pack()
        # Create widgets
        self._create_form()
        
    def _create_form(self):
        fields = ["Username", "Password"]
        labels = [tk.Label(self, text=f) for f in fields]
        self.entries = [tk.Entry(self, textvariable = tk.StringVar()) for _ in fields]
        self.widgets = list(zip(labels, self.entries))
        for i, (label, entry) in enumerate(self.widgets): ### CREATE A FUNCTION TO REPLACE THIS REPEATED CODE?
            label.grid(row=i, column=0, padx=10, sticky=tk.W)
            entry.grid(row=i, column=1, padx=10, pady=5)

    def get_details(self):
        return [e.get() for e in self.entries]

class EventWidget(tk.Frame):
    def __init__(self, master):
        self.master = master
        self._create_buttons() 
        
    def _create_buttons(self):
        states = ({'text':'Submit'},
                  {'text':'Register', 'fg':'red', 'relief':'flat'}
                  )
        self.buttons = [tk.Button(self.master, **f) for f in states]
        for i, button in enumerate(self.buttons):
            button.grid(row=len(self.master.widgets)+i, column=1, columnspan=1, padx=10)
            
    def attach(self, observer):
        commands = [observer.Submit, 
                    observer.Register]
        for i, button in enumerate(self.buttons): ### USe mapping instead
            button.config(command=commands[i])     