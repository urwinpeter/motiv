
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
        self.items = [] # Do I need this>?
        self.selection = None
        self._view_items()

    def _view_items(self):
        self.items = list(self.calc.get_items())
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
        # Create new Item instance and give it same rowID  
        rowid = self.items[self.selection].rowid
        updated_item = self.view.get_details()
        updated_item.rowid = rowid
        # send updated item to db:
        self.calc.update_item(updated_item)
        self.items[self.selection] = updated_item # replace item with updated item in self.items list
        self.view.update_item(updated_item, self.selection) # display the update item in listbox at appropriate index position

    def delete_item(self):
        print('delete')
        if not self.selection:
            return
        item = self.items[self.selection]
        self.calc.delete_item(item)
        self.view.remove_items()
        self._view_items()
        
    def load_homepage(self):
        print('load')
        item = self.view.get_details()
        model = HomeCalculator(self.view.get_salary(), item)
        self.view.destroy()
        view = HomePage(self.root)
        app = HomeController(self.root, model, view, item)

class HomeController(Controller):
    def __init__(self, root, model, view, item):
        super().__init__(root, model, view)
        # Attach controller as observer of earnings
        self.calc.earnings.attach(self)
        # Set initial counting state
        self.count = False
        # Set initial earnings
        self.view.set_target(float(item.price))
        self.update(self.calc.earnings.val)
        self.item = item 
        
        
        # Attach controller to manage callbacks 
        self.quote = self.calc.get_quote()
        self.view.display_quote(self.quote)   

           
    ######
    #CALLED FROM VIEW
    ######
    def Start(self, event=None):
        self._start_time = time.time()
        self._AddMoney(self._start_time)
        
    def _AddMoney(self, time):
        self.count = True
        self.calc.addMoney(time)
        self.view.update_count(self.count)

    def PauseMoney(self, event=None):
        self.count = False
        self.view.update_count(self.count)

    def ResetMoney(self, event=None):
        self.count = None
        self.calc.resetMoney()
        self.view.update_count(self.count)

    ######
    #CALLED FROM MODEL
    ######
    def update(self, money):
        self.view.update_money(money)
        self.view.after(100, lambda : self._AddMoney(self._start_time) 
                            if self.count == True  else None) # or use observer.attach/detach in pausemoney/resetmoney etc
    
    def mission_accomplished(self, money):
        self.view.update_money(money)
        self.view.update_count(self.count) ##change this to False?
        self.view.display_congrats(self.item)
        #observer.detach?