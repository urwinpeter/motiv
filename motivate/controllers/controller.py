from motivate.views.widgets import *
from motivate.models.models import *

class Controller():
    def __init__(self, root, model, view1, view2):
        # Make controller aware of models and views
        self.root = root # should i set this as a class variable since it will be same for all instances?
        self.calc = model
        self.view1 = view1
        self.view2 = view2
        
class LoginController(Controller):
    def __init__(self, root, model, view1, view2):
        super().__init__(root, model, view1, view2)

    def Submit(self):
        contact = self.view1.get_details() 
        if not contact:
            return
        try:
            salary = self.calc.request_salary(contact)[0]
        except TypeError:
            self.view1.error("Incorrect Login Details")
            return

        self.view1.destroy()
        fields = ['My Earnings']
        states = ({'text':'Start',},
        {'text':'Pause'},
        {'text':'Reset'})
        model = HomeCalculator(salary)
        view1 = HomeForm(self.root, fields)
        view2 = HomeEventWidget(view1, states)
        app = HomeController(self.root, model, view1, view2)
        commands = [app.Start,
                app.PauseMoney,
                app.ResetMoney]
        view2.set_ctrl(commands)
    
    def Register(self):
        self.view1.destroy()
        fields = ["Username", "Password", "Salary"]
        states = ({'text':'Submit'},)
        model = RegisterCalculator()
        view1 = Form(self.root, fields)
        view2 = EventWidget(view1, states)
        app = RegisterController(self.root, model, view1, view2)
        commands = [app.Submit]
        view2.set_ctrl(commands)
        
class RegisterController(Controller):
    def __init__(self, root, model, view1, view2):
        super().__init__(root, model, view1, view2)

    def Submit(self):
        contact = self.view1.get_details() 
        if not contact:
            return
        self.calc.addcontact(contact)
        self.view1.destroy()

        fields = ["Username", "Password"]
        states = ({'text':'Submit'},
            {'text':'Register', 'fg':'red', 'relief':'flat'}
                  )
        model = LoginCalculator()              
        view1 = Form(self.root, fields)
        view2 = EventWidget(view1, states)
        app = LoginController(self.root, model, view1, view2)
        commands = [app.Submit, 
                app.Register]
        view2.set_ctrl(commands)
        
class HomeController(Controller):
    def __init__(self, root, model, view1, view2):
        super().__init__(root, model, view1, view2)
        # Attach controller as observer of earnings
        self.calc.earnings.attach(self)
        # Set initial counting state
        self.count = False
        # Set initial earnings
        self.update(self.calc.earnings.val)

    def Start(self):
        self._start_time = time.time()
        self._AddMoney(self._start_time)
        
    def _AddMoney(self, time):
        self.count = True
        self.calc.addMoney(time)

    def PauseMoney(self):
        self.count = False
        self.view2.SetCount(self.count)

    def ResetMoney(self):
        self.count = None
        self.calc.resetMoney()

    def update(self, money):
        self.view1.SetMoney(money)
        self.view2.SetCount(self.count)
        self.view1.after(100, lambda: self.AddMoney(self._start_time) 
                            if self.count == True else None)
        