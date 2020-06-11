# Standard library imports
import logging
import time
# Local applications imports
from motivate.logs import log_user_actions

_log= logging.getLogger('motivate.controllers.controller')


class ItemController():
    def __init__(self, item_service):
        self.item_service = item_service

    def get_items(self):
        return self.item_service.get_items()
                    
    @log_user_actions(_log) 
    def on_item_select(self, index):
        self.item_service.select_item(index)
    
    @log_user_actions(_log)   
    def on_save_button_click(self, new_item): 
        self.item_service.create_item(new_item)
        
    @log_user_actions(_log)
    def on_update_button_click(self, updated_item):
        self.item_service.update_item(updated_item)

    @log_user_actions(_log)
    def on_delete_button_click(self):
        self.item_service.delete_item()
    
        
