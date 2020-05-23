import tkinter as tk

class View(tk.Frame):
    def __init__(self, master):
        super().__init__(master, width = 30)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text='My Earnings').grid(row=0, columnspan=2, column=0)
        self.moneyCtrl = tk.Entry(self, width=8)
        self.moneyCtrl.grid(row=0, column=2)
        
    def SetMoney(self, money):
        self.moneyCtrl.delete(0,'end')
        self.moneyCtrl.insert('end', str(money))        

class EventWidget(tk.Frame):
    def __init__(self, master):
        self.master = master
        self._create_buttons() 
        
    def _create_buttons(self):
        fields = ["Start", "Pause", "Reset"]          
        self.buttons = [tk.Button(self.master, width = 8, text = f) for f in fields]
        for i, button in enumerate(self.buttons):
            button.grid(row=2, column=i)
            
    def attach(self, observer):
        commands = [observer.AddMoney, 
                    observer.PauseMoney,
                    observer.ResetMoney]
        for i, button in enumerate(self.buttons):
            button.config(command=commands[i])

    def SetCount(self, count):
        combos = {True: (tk.DISABLED, tk.ACTIVE, tk.DISABLED),
                False: (tk.ACTIVE, tk.DISABLED, tk.ACTIVE),
                None: (tk.ACTIVE, tk.DISABLED, tk.DISABLED)}
        for i, button in enumerate(self.buttons):
            button.config(state=combos[count][i])

    
