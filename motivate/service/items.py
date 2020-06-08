
import motivate.models.database as database

class ItemService:
    
    def __init__(self):
        super().__init__()
        self.items_db = database.ItemsDB()               

    def create_item(self, new_item): 
        if new_item:
            self.items_db.add_item(item=new_item) # The add_item function also furnishes item object with appropriate rowid
            self.items.append(item=new_item)           

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

    def delete_item(self, item):
        self.items_db.delete_item(item)