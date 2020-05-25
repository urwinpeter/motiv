from motivate.views.views import Form, HomeForm, EventWidget HomeEventWidget

'''ideas - replace all 3 with one universal function
        - replace with a class
        - replace with contact like class
        - replace with appstate like class

class AppState():
    def __init__(self, model, view1, view2, controller):
        self._mvc = [model, view1, view2, controller]
        
    @property
    def details(self):
        return self._mvc

    @details.setter
    def details(self, value):
        self._mvc = value'''

def start_home():
    fields = ['My Earnings']
    states = ({'text':'Start',},
            {'text':'Pause'},
            {'text':'Reset'})
    model = HomeCalculator()
    view1 = HomeForm(root, fields)
    view2 = HomeEventWidget(view1, states)
    app = HomeController(root, model, view1, view2)
    commands = [model.AddMoney,
                model.PauseMoney,
                model.ResetMoney]
    view2.set_ctrl(commands)

    
    
    
    return model, view1, view2, commands

    
def start_login(root, observer):
    fields = ["Username", "Password"]
    states = ({'text':'Submit'},
            {'text':'Register', 'fg':'red', 'relief':'flat'}
                  )
    model = LoginCalculator()              
    view1 = Form(root, fields)
    view2 = EventWidget(view1, states)
    app = LoginController(root, model, view1, view2)
    commands = [app.Submit, 
                app.Register]
    view2.set_ctrl(commands)



def start_register(root):
    fields = ["Username", "Password", "Salary"]
    states = ({'text':'Submit'},)
    model = RegisterCalculator
    view1 = Form(root, fields)
    view2 = EventWidget(view1, states)
    commands = [observer.Submit]
    view2.set_ctrl(commands)

    return model, view1, view2, commands
    