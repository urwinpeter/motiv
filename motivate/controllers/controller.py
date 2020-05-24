
class Controller():
    def __init__(self, root, model, view1, view2):
        # Make controller aware of models and views
        self.root = root # should i set this as a class variable?
        self.calc = model
        self.view1 = view1(root)
        self.view2 = view2(self.view1)
        # Attach controller as observer of button widgets
        #self.view2.attach(self)

class LoginController(Controller):
    def __init__(self, root):
        super().__init__(root)
         
    def Submit(self):
        if self.calc.check(*self.view1.get_details()) == True:
            self.view1.destroy()
            HomeController(self.root, home_start())
        else:
            print('Incorrecto')

    def Register(self):
        self.view1.destroy()
        RegisterController(self.root, register_start())

class RegisterController(Controller):
    def __init__(self, root):
        super().__init__(root)

    def Submit(self):
        self.calc.addcontact(self.view1.get_details())
        self.view1.destroy()
        LoginController(self.root, login_start())

class HomeController(Controller):
    def __init__(self, root):
        super().__init__(root)
        # Attach controller as observer of earnings
        self.calc.earnings.attach(self)
        # Set initial earnings
        self.update(self.calc.earnings, False)

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
