# Third party imports
from pubsub import pub
# Local application imports
from motivate.models.database import ItemsDB


class ItemService():
    def __init__(self):
        self.items_db = ItemsDB()
        self.item_selection = None
        self.items = list(self.items_db.get_items())              
        
    def get_items(self):
        return self.items

    def select_item(self, index):
        self.item_selection = index  
        self._notify("item_selected", item=self.items[self.item_selection])
   
    def create_item(self, new_item): 
        self.items_db.add_item(new_item)
        self.items.append(new_item) 
        #self._notify("item_created", item=new_item)
            
    def update_item(self, updated_item):
        if self.item_selection == None:
            return
        rowid = self.items[self.item_selection].rowid
        updated_item.rowid = rowid
        self.items[self.item_selection] = updated_item
        self.items_db.update_item(updated_item)
        #self._notify("item_updated", updated_item=updated_item)
        
    def delete_item(self):
        if self.item_selection == None:
            return
        self.items_db.delete_item(self.items[self.item_selection])
        del self.items[self.item_selection]
        #self.item_selection = 0 
        #self._notify()

    def _notify(self, message, **kwargs):
        pub.sendMessage(message, **kwargs)