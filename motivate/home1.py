import tkinter as tk
import time


class Observable():
    def __init__(self):
        self._earnings = 0
        self._observers = []
        
    def attach(self, observer) -> None:
        print("attached observer " + str(observer))
        self._observers.append(observer)

    def detach(self, observer) -> None:
        self._observers.remove(observer)

    def _notify(self, earnings) -> None:
        print("notifying observers..")
        for observer in self._observers:
            observer.update(earnings)

    @property
    def earnings(self):
        return self._earnings

    @earnings.setter
    def earnings(self, earnings):
        self._earnings = earnings
        self._notify(self._earnings)
   
class Calculator():
    def __init__(self):
        salary = 1_000_000
        self.obs = Observable()
        self._rate = salary / (365 * 24 * 60 * 60)
        self._start_time = time.time()
        
    def addMoney(self):
        earnings = self._rate * (time.time() - self._start_time)
        self.obs.earnings = (self.obs.earnings + earnings)

    def removeMoney(self, value):
        self.obs.earnings = (self.obs.earnings - value)


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
        self.removeButton = tk.Button(self, text='Remove', width=8)
        self.removeButton.pack(side='left')   
        self.pack()     


class Controller():
    def __init__(self, root):
        self.calc = Calculator()
        self.calc.obs.attach(self)
        self.view1 = View(root)
        self.view2 = ChangerWidget(root)
        self.view2.addButton.config(command=self.AddMoney)
        self.view2.removeButton.config(command=self.RemoveMoney)
        self.update(self.calc.obs.earnings)
        
        
    def AddMoney(self):
        self.calc.addMoney()

    def RemoveMoney(self):
        self.calc.removeMoney(10)

    def update(self, money):
        self.view1.SetMoney(money)

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('500x500')
    root.title("Let's Get Pumped!")
    app = Controller(root)
    root.mainloop()

