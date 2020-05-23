from motivate.models.model import Calculator
from motivate.views.login import Login, EventWidget
import motivate.controllers.home

class Controller():
    def __init__(self, root):
        # Make controller aware of models and views
        #self.calc = Calculator()
        self.root = root
        self.view1 = Login(root)
        self.view2 = EventWidget(self.view1)

        # Attach controller as observer of models and views
        #self.calc.obs.attach(self)
        self.view2.attach(self)

        # Set initial earnings
        #self.update(self.calc.obs.earnings, False)
          
    def Submit(self):
        self.view1.destroy()
        motivate.controllers.home.Controller(self.root)

    def Register(self):
        print("ToDo")

    def update(self, money, count):
        self.view1.SetMoney(money)
        self.view2.SetCount(count)
        if count == True:
            self.view1.after(100, self.AddMoney)
            