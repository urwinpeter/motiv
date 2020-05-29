import tkinter as tk

class EventWidget(tk.Frame):
    def __init__(self, master, fields):
        super().__init__(master)
        self._create_buttons(fields) 
        
    def _create_buttons(self, fields):
        self.buttons = [tk.Button(self, **f) for f in fields]
        for i, button in enumerate(self.buttons):
            button.grid(row=0, column=i, columnspan=1, padx=10)
    
    def set_ctrl(self, commands):
        for i, button in enumerate(self.buttons): 
            button.config(command=commands[i])
            button.bind("<Return>", commands[i])

class HomeEventWidget(EventWidget):
    fields = {'text':'Start'}, {'text':'Pause'}, {'text':'Reset'}
    def __init__(self, master):
        super().__init__(master, self.fields) 
        
    def set_ctrl(self, observer):
        commands = observer.Start, observer.PauseMoney, observer.ResetMoney
        super().set_ctrl(commands)

    def SetCount(self, count):
        combos = {True: (tk.DISABLED, tk.ACTIVE, tk.DISABLED),
                False: (tk.ACTIVE, tk.DISABLED, tk.ACTIVE),
                None: (tk.ACTIVE, tk.DISABLED, tk.DISABLED)}
        for i, button in enumerate(self.buttons):
            button.config(state=combos[count][i])

class ItemEventWidget(EventWidget):
    fields = {'text':'Save'}, {'text':'Delete'}, {'text':'Set As Motivation >'}
    def __init__(self, master):
        super().__init__(master, self.fields)

class SetSalaryEventWidget(EventWidget):
    fields = {'text':'Next >'},
    def __init__(self, master):
        super().__init__(master, self.fields)

    

