import time
import logging
from motivate.logs import log_user_actions
from motivate.models.calculator import EarningsCalculator
from motivate.models.database import ItemsDB, QuotesDB

_log= logging.getLogger(__name__)

class LoginController():
    def __init__(self, master_controller, root_widget):
        self.master_control = master_controller
        self.items_db = ItemsDB()              
        self.login_view = LoginPage(root_widget)
        self.login_view.assign_callbacks(
                                        control=self, 
                                        mastercontrol=self.master_control # or just master controller?
                                        ) 
        #self.items = [] # do i need this?
        self.items = list(self.items_db.get_items())
        self._view_items()
        self.item_selection = None

    def _view_items(self): 
        for item in self.items:
            self.login_view.append_item(item)

    @log_user_actions(_log)    
    def select_item(self, index):
        self.item_selection = index
        item = self.items[index]
        self.login_view.display_item_details(item)        

    @log_user_actions(_log)
    def create_item(self, event=None): 
        new_item = self.login_view.get_item_details()
        if new_item:
            self.items_db.add_item(item=new_item) # The add_item function also furnishes item object with appropriate rowid
            self.items.append(item=new_item)          
            self.login_view.append_item(item=new_item)       

    @log_user_actions(_log)
    def update_item(self, event=None):
        if self.item_selection == None:
            return
        rowid = self.items[self.item_selection].rowid
        updated_item = self.login_view.get_item_details()
        if updated_item:
            updated_item.rowid = rowid
            self.items_db.update_item(updated_item)
            self.items[self.item_selection] = updated_item 
            self.login_view.update_item(
                                        item=updated_item, 
                                        index=self.item_selection
                                        ) 

    @log_user_actions(_log)
    def delete_item(self, event=None):
        if self.item_selection == None:
            return
        item = self.items[self.item_selection]
        self.items_db.delete_item(item)
        self.login_view.remove_items()
        self._view_items()

    
class HomePageController():
    def __init__(self, master_widget):
        self.master_widget = master_widget)
        ViewManager.bind_next(load_homepage)

    def load_homepage(self, salary, item):
        price = float(item.price)
        quote = QuotesDB().get_quote()
        self.item = item
        self.calculator = EarningsCalculator(salary, price)
        self.calculator.attach(observer=self)
        self.home_view = HomePage(quote, price, self.master_widget)
        self.home_view.assign_callbacks(
                                        control=self
                                        )
        self._counting_status = False
        self.update_earnings(0)
        
    def start(self, event=None):
        self._start_time = time.time()
        self._add_money(self._start_time)
        
    def _add_money(self, time):
        self._counting_status = True
        (amount, complete) = self.calculator.add_money(time)
        if complete:
            self.home_view.update_earnings(amount)
            view.exit(self.item.name)
        else:
            self.home_view.update_status(self._counting_status)

    def pause_money(self, event=None):
        self._counting_status = False

    def reset_money(self, event=None):
        self._counting_status = None
        self.calculator.reset_money()
        self.home_view.update_status(self._counting_status)

    def update_earnings(self, money):
        self.home_view.update_earnings(money)
        self.home_view.after(100, 
                            lambda : self._add_money(self._start_time) 
                            if self._counting_status == True  
                            else None
                            ) # or use observer.attach/detach in pausemoney/resetmoney etc
