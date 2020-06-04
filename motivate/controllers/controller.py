import time
import logging
from motivate.logs import log_user_actions
from motivate.models.calculator import EarningsCalculator
from motivate.models.database import ItemsDB, QuotesDB
from motivate.views.pages import LoginPage, HomePage

_log= logging.getLogger(__name__)

class PageController():
    """
    The master controller. Used to start/stop the app and designate control 
    to secondary controllers.

    ...

    Attributes
    ----------
    root_widget : tkinter.TK
        The main window on which Pages are placed
    login_control : LoginController object
        Controls all events unique to the LoginPage
    home_control : HomeController object
        Controls all events unique to the HomePage
    """

    def __init__(self, root_widget):
        self.root_widget = root_widget
        self.login_control = LoginPageController(self, root_widget)
        self.home_control = HomePageController(self, root_widget)

    def start_app(self):
        """Sets mainloop in motion"""
        self.root_widget.mainloop()

    def load_homepage(self, event=None):
        """Destroys LoginPage and loads HomePage""" 
        salary = self.login_control.login_view.get_salary() # this seems like a cheat
        item = self.login_control.login_view.get_item_details() # as does this
        if item and salary:
            self.login_control.login_view.destroy()
            self.home_control.load_homepage(salary, item)

    def terminate_app(self):
        """Terminates App"""
        self.root_widget.destroy() # is this sort of format ok?


class LoginPageController():
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
    def __init__(self, master_controller, master_widget):
        self.master_control = master_controller
        self.master_widget = master_widget

    def load_homepage(self, salary, item):
        price = float(item.price)
        quote = QuotesDB().get_quote()
        self.item = item
        self.calculator = EarningsCalculator(salary, price)
        self.calculator.attach(observer=self)
        self.home_view = HomePage(quote, price, self.master_widget)
        self.home_view.assign_callbacks(
                                        control=self, 
                                        mastercontrol=self.master_control
                                        )
        self._counting_status = False
        self.update_earnings(0)
        
    def start(self, event=None):
        self._start_time = time.time()
        self._add_money(self._start_time)
        
    def _add_money(self, time):
        self._counting_status = True
        self.calculator.add_money(time)
        self.home_view.update_status(self._counting_status)

    def pause_money(self, event=None):
        self._counting_status = False
        self.home_view.update_status(self._counting_status)

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
    
    def mission_accomplished(self, money):
        self._counting_status = False
        self.home_view.update_earnings(money)
        self.home_view.update_status(False) 
        self.home_view.display_congrats(self.item.name)
        self.master_control.terminate_app() 