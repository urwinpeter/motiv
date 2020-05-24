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
    model = LoginCalculator()
    fields = ['My Earnings']
    states = ({'text':'Start'},
            {'text':'Pause'},
            {'text':'Reset'})
    view1 = HomeForm(root, fields)
    view2 = HomeEventWidget(view1, states)
    return model, view1, view2

    commands = [observer.AddMoney,
                observer.PauseMoney,
                observer.ResetMoney]

def start_login(root):
    fields = ["Username", "Password"]
    states = ({'text':'Submit'},
            {'text':'Register', 'fg':'red', 'relief':'flat'}
                  )
    view1 = Form(root, fields)
    view2 = EventWidget(view1, states)


    commands = [observer.Submit, 
                observer.Register]

def start_register(root):
    fields = ["Username", "Password", "Salary"]
    states = ({'text':'Submit'},)
    view1 = Form(root, fields)
    view2 = EventWidget(states)

    commands = [observer.Submit]