# Standard library imports
import logging

_log= logging.getLogger(__name__)

class MoneyController():
    def __init__(self, money_service):
        self.money_service = money_service
    
    def load(self, salary, price):
        self.money_service.set_user_values(salary, price)
        
    def start(self):
        self.money_service.add_money()

    def pause_money(self):
        self.money_service.pause_money()
    
    def reset_money(self):
        self.money_service.reset_money()
    
