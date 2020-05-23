from motivate.models.login import Calculator
from motivate.views.login import Login, EventWidget
import motivate.controllers.home
import motivate.controllers.register


class Controller():
    def __init__(self, root):
        # Make controller aware of models and views
        self.calc = Calculator()
        self.root = root
        self.view1 = Login(root)
        self.view2 = EventWidget(self.view1)
        # Attach controller as observer of models and views
        self.view2.attach(self)
         
    def Submit(self):
        if self.calc.check(*self.view1.get_details()) == True:
            self.view1.destroy()
            motivate.controllers.home.Controller(self.root)
        else:
            print('Incorrecto')
    
    def Register(self):
        self.view1.destroy()
        motivate.controllers.register.Controller(self.root)

            