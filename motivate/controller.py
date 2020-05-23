from motivate.model import Calculator
from motivate.view import View, ChangerWidget

class Controller():
    def __init__(self, root):
        self.calc = Calculator()
        self.calc.obs.attach(self)
        self.view1 = View(root)
        self.view2 = ChangerWidget(root)
        self.view2.addButton.config(command=self.AddMoney)
        self.view2.pauseButton.config(command=self.PauseMoney)
        self.view2.resetButton.config(command=self.ResetMoney)
        self.update(self.calc.obs.earnings, False)
          
    def AddMoney(self):
        self.calc.addMoney()

    def PauseMoney(self):
        self.calc.pauseMoney()

    def ResetMoney(self):
        self.calc.resetMoney()

    def update(self, money, count):
        self.view1.SetMoney(money)
        if count == True:
            self.view1.after(100, self.AddMoney)
            

