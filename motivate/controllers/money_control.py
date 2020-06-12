# Standard library imports
import logging

_log = logging.getLogger(__name__)


class MoneyController():
    def __init__(self, money_service, quote_service):
        self.money_service = money_service
        self.quote_service = quote_service
    
    def on_next_button_click(self, salary, price):
        self.money_service.set_user_values(salary, price)
        self.money_service.set_initial_earnings()
        self.quote_service.get_quote()
        
    def on_start_button_click(self):
        self.money_service.add_money()

    def on_pause_button_click(self):
        self.money_service.pause_money()
    
    def on_reset_button_click(self):
        self.money_service.reset_money()
    
