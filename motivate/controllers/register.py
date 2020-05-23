from motivate.models.register import Calculator
from motivate.views.register import Register, EventWidget
import motivate.controllers.home

class Controller():
    def __init__(self, root):
        # Make controller aware of models and views
        self.calc = Calculator()
        self.root = root
        self.view1 = Register(root)
        self.view2 = EventWidget(self.view1)
        # Attach controller as observer of models and views
        self.view2.attach(self)
         
    def Submit(self):
        self.view1.destroy()
        motivate.controllers.home.Controller(self.root)
