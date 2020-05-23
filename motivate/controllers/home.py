from motivate.models.model import Calculator
from motivate.views.home import View, EventWidget

class Controller():
    def __init__(self, root):
        # Make controller aware of models and views
        self.calc = Calculator()
        self.view1 = View(root)
        self.view2 = EventWidget(self.view1)

        # Attach controller as observer of models and views
        self.calc.obs.attach(self)
        self.view2.attach(self)

        # Set initial earnings
        self.update(self.calc.obs.earnings, False)
          
    def AddMoney(self):
        self.calc.addMoney()

    def PauseMoney(self):
        self.calc.pauseMoney()

    def ResetMoney(self):
        self.calc.resetMoney()

    def update(self, money, count):
        self.view1.SetMoney(money)
        self.view2.SetCount(count)
        if count == True:
            self.view1.after(100, self.AddMoney)
            