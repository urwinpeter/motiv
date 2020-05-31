from motivate.models.models import HomeCalculator
from motivate.models.database import ItemsDB, QuotesDB
from motivate.views.pages import LoginPage, HomePage

class PageController():
    def __init__(self):
        self.login = LoginController(self)
        self.home = HomeController(self)

    def start_login(self):
        self.login.view.start()

    def pass_control(self, salary, item):
        salary = self.login.view.get_salary()
        item = self.login.view.get_details()
        self.login.view.destroy()
        self.home.load(salary, item)
  
class LoginController():
    def __init__(self, parent):
        self.parent = parent
        self.calc = ItemsDB()              
        self.view = LoginPage()
        self.view.assign_callbacks(self)
        
        self.items = list(self.calc.get_items())
        self.selection = None
        self._view_items()

    def _view_items(self): 
        for c in self.items:
            self.view.add_item(c)

    def create_item(self): 
        new_item = self.view.get_details()
        self.calc.add_item(new_item)        # Add item to DB
        self.items.append(new_item)          
        self.view.add_item(new_item)        # Display item in listbox
        
    def select_item(self, index):
        self.selection = index
        item = self.items[index]
        self.view.load_details(item)

    def update_item(self):
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
        if not self.selection:
            return
        item = self.items[self.selection]
        self.calc.delete_item(item)
        self.view.remove_items()
        self._view_items()
        
class HomeController():
    def __init__(self, parent):
        self.parent = parent

    def load(self, salary, item):
        price = float(item.price)
        quote = QuotesDB().get_quote()
        self.calc = HomeCalculator(salary, price)
        self.calc.earnings.attach(self)
        self.view = HomePage(quote, price)
        self.view.assign_callbacks(self) # Assign controller to manage callbacks 
        
        # Set initial counting state and earnings value
        self.count = False
        self.update(0) # could i mitigate this by setting it to 0 in view from get go?
        self.item = item
             
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
        self.view.display_congrats(self.item) # this is the second time i've passed item to view. should I just pass it once
        #observer.detach? # or cahnge this to self.item.name