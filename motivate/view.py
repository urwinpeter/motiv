import tkinter as tk

class View(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        #self.protocol('WM_DELETE_WINDOW', self.master.destroy)
        tk.Label(self, text='My Money').pack(side='left')
        self.moneyCtrl = tk.Entry(self, width=8)
        self.moneyCtrl.pack(side='left')
        self.pack()
        
    def SetMoney(self, money):
        self.moneyCtrl.delete(0,'end')
        self.moneyCtrl.insert('end', str(money))        


class ChangerWidget(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.addButton = tk.Button(self, text='Add', width=8)
        self.addButton.pack(side='left')
        self.pauseButton = tk.Button(self, text='Pause', width=8)
        self.pauseButton.pack(side='left') 
        self.resetButton = tk.Button(self, text='Reset', width=8)
        self.resetButton.pack(side='left')  
        self.pack()     