# Standard library imports
import time
import logging

# Local applications imports
from motivate.logs import log_user_actions


_log= logging.getLogger(__name__)

class ItemController():
    def __init__(self, item_service):
        self.item_service = item_service
                    
    @log_user_actions(_log)
    def select_item(self, index):
        self.item_service.select_item(index)
    
    @log_user_actions(_log)   
    def create_item(self, new_item): 
        self.item_service.create_item(new_item)
        
    @log_user_actions(_log)
    def update_item(self, updated_item):
        self.item_service.update_item(updated_item)

    @log_user_actions(_log)
    def delete_item(self):
        self.item_service.delete_item()
    
        
