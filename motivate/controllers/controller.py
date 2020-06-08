import time
import logging
from motivate.logs import log_user_actions
from motivate.models.calculator import EarningsCalculator
from motivate.models.database import ItemsDB, QuotesDB
from motivate.views.pages import LoginPage, HomePage

_log= logging.getLogger(__name__)

class LoginController():
    def __init__(self):
        self.items_db = ItemsDB()              
        self.items = list(self.items_db.get_items())
        #self._view_items()
        self.item_selection = None

    '''def _view_items(self): 
        for item in self.items:
            self.login_view.append_item(item)'''

    @log_user_actions(_log)    
    def select_item(self, index, con):
        self.item_selection = index
        item = self.items[index]
        con.display_item_details(item)        

    @log_user_actions(_log)   
    def create_item(self, new_item, con): 
        self.items_db.add_item(item=new_item) # The add_item function also furnishes item object with appropriate rowid
        self.items.append(new_item)          
        con.append_item(item=new_item)     

    @log_user_actions(_log)
    def update_item(self, updated_item, con):
        if self.item_selection == None:
            return
        rowid = self.items[self.item_selection].rowid
        #updated_item = con.get_item_details()
        updated_item.rowid = rowid
        self.items_db.update_item(updated_item)
        self.items[self.item_selection] = updated_item 
        con.update_item(
                        item=updated_item, 
                        index=self.item_selection
                        ) 
    

    #@log_user_actions(_log)
    def delete_item(self, con):
        if self.item_selection == None:
            return
        item = self.items[self.item_selection]
        self.items_db.delete_item(item)
        con.remove_items()
        #self._view_items() change to a con._view_items

class HomeController():
    def __init__(self):
        self._counting_status = False
    
    def load(self, salary, price):
        # self.home_view = view ----Could pass view in here instead
        self.calculator = EarningsCalculator(salary, price) # chagne this so calculator has update function for receiving salary+price
        
    def start(self, view):
        
        self._start_time = time.time()
        self._counting_status = True
        self._add_money(self._start_time, view)
        
    def _add_money(self, time, view):
        money = self.calculator.add_money(time)
        view.update_earnings(money)
        view.after(100, 
                lambda : self._add_money(self._start_time, view) 
                if self._counting_status == True  
                else None
                )
        
    def pause_money(self, view):
        self._counting_status = False
    
    def reset_money(self, view):
        self._counting_status = False
        self.calculator.reset_money()
        view.update_earnings(0)
        

'''class PageController():
    def __init__(self, root_widget):
        self.root_widget = root_widget
        self.login_view = LoginPage(root_widget)
        self.home_view = HomeView(root_widget)
        self.login_control = LoginPageController(self, self.login_view)
        self.home_control = HomePageController(self, self.home_view)

    def assign(self):
        self.login_view.assign_callbacks(self.login_control)
        self.home_view.assign_callbacks(self.home_control)

    def start_app(self):
        """Sets mainloop in motion"""
        self.login_view.tkraise()
        self.root_widget.mainloop()

    def load_homepage(self, item, salary):
        """Destroys LoginPage and loads HomePage""" 
        
        self.home_control.update(item, salary)
        self.home_view.tkraise()

    def terminate_app(self):
        """Terminates App"""
        self.root_widget.destroy()'''
