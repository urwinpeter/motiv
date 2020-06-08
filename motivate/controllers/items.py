

class ItemController():

    def __init__(self, item_service):     
        self._item_service = item_service

        #self.items = [] # do i need this?
        self.items = list(self.items_db.get_items())
        self._view_items()
        self.item_selection = None

    def get_items(self): 
        self._item_service.get_items()

    @log_user_actions(_log)    
    def select_item(self, index):
        pass    

    @log_user_actions(_log)
    def create_item(self, item): 
        self._item_service.create_item(item)       

    @log_user_actions(_log)
    def update_item(self, item):
        self._item_service.update_item(item)

    @log_user_actions(_log)
    def delete_item(self, item):
        self._item_service.delete_item(item)
