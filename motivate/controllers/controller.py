
from motivate.models.models import *
from motivate.views.pages import HomePage

class Controller():
    def __init__(self, root, model, view):
        # Make controller aware of models and views
        self.root = root # should i set this as a class variable since it will be same for all instances?
        self.calc = model
        self.view = view
        # Attach controller to manage callbacks
        self.view.assign_callbacks(self)
        
class LoginController(Controller):
    def __init__(self, root, model, view):
        super().__init__(root, model, view)
        self.items = list(model.get_items()) # should this be here or in _load_items
        self.selection = None
        self._load_items()

    def _load_items(self):
        for c in self.items:
            self.view.add_item(c)

    def create_item(self):
        new_item = self.view.get_details()
        self.calc.add_item(new_item)        # Add item to DB
        self.items.append(new_item)          
        self.view.add_item(new_item)        # Display item in listbox
        
    def select_item(self, index):
        print('select')
        self.selection = index
        item = self.items[index]
        self.view.load_details(item)

    def update_item(self):
        print('update')
        if not self.selection:
            return
        # Create new Item instance and override rowID  
        rowid = self.items[self.selection].rowid
        updated_item = self.view.get_details()
        updated_item.rowid = rowid
        # send updated item to db:
        self.calc.update_item(updated_item)
        self.items[self.selection] = update_item # replace item with updated item in self.items list
        self.view.update_item(item, self.selection) # display the update item in listbox at appropriate index position

    def delete_item(self):
        print('delete')
        if not self.selection:
            return
        item = self.items[self.selection]
        self.calc.delete_item(item)
        self.view.remove_item(self.selection)

    #def set_item(self): # should i add instance of item class and setters/getters?
        #print('setting')

    def load_homepage(self):
        print('load')
        model = HomeCalculator(self.view.get_salary())
        self.view.destroy()
        view = HomePage(self.root)
        app = HomeController(self.root, model, view, int(self.items[self.selection].cost))

class HomeController(Controller):
    def __init__(self, root, model, view, target):
        super().__init__(root, model, view)
        # Attach controller as observer of earnings
        self.calc.earnings.attach(self)
        # Set initial counting state
        self.count = False
        # Set initial earnings
        self.calc.set_target(target)
        self.update(self.calc.earnings.val)
        
        # Attach controller to manage callbacks 
        #self.quote = self.calc.get_quote()
        #self.view.display_quote(self.quote)      
    
    ######
    #CALLED FROM VIEW
    ######
    def Start(self, event=None):
        self._start_time = time.time()
        self._AddMoney(self._start_time)
        
    def _AddMoney(self, time, event=None):
        self.count = True
        self.calc.addMoney(time)

    def PauseMoney(self, event=None):
        self.count = False
        self.view.SetCount(self.count)

    def ResetMoney(self, event=None):
        self.count = None
        self.calc.resetMoney()

    ######
    #CALLED FROM MODEL
    ######
    def update(self, money, event=None):
        self.view.SetMoney(money)
        self.view.SetCount(self.count)
        self.view.after(100, lambda: self._AddMoney(self._start_time) 
                            if self.count == True else None)
    
    def complete(self):
        self.view.congrats()

    def set_target(self, value):
        self.view.set_target(value)

    '''def Submit(self, event=None):
        item = self.view.get_details() 
        if not item:
            return
        try:
            salary = self.calc.request_salary(item)[0]
        except TypeError:
            self.view.error("Incorrect Login Details")
            return'''

        
class RegisterController(Controller):
    def __init__(self, root, model, view1, view2):
        super().__init__(root, model, view1, view2)

    def Submit(self, event=None):
        item = self.view1.get_details() 
        if not item:
            return
        self.calc.additem(item)
        self.view1.destroy()

        fields = ["Username", "Password"]
        states = ({'text':'Submit'},
            {'text':'Register', 'fg':'red', 'relief':'flat'}
                  )
        model = LoginCalculator()              
        view1 = Form(self.root, fields)
        view2 = LoginEventWidget(view1, states)
        app = LoginController(self.root, model, view1, view2)
        






