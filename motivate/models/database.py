# Standard library imports
import logging

# Third party imports
import sqlalchemy as sa

# Local application imports
from motivate.logs import log_db_changes, log_db_items
from motivate.item import DBItem

_log = logging.getLogger(__name__)

class UseDatabase():
    """Context manager to manage connection with database"""
    def __init__(self, db_config):
        self.engine = sa.create_engine(db_config)

    def __enter__(self):
        self.conn = self.engine.connect() 
        return self.conn
        
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.conn.close()


class ItemsDB():
    config = 'sqlite:///motivate/models/items.db'

    def __init__(self):
        self.conn = UseDatabase(self.config)

    def _to_values(self, c):
        return c.category, c.name, c.price

    @log_db_changes(_log)
    def add_item(self, item):
        _sql = """INSERT INTO items VALUES
                (?, ?, ?)"""
        with self.conn as conn:
            rowid = conn.execute(
                                _sql,
                                self._to_values(item)
                                ).lastrowid
            item.rowid = rowid # the newly created item needs to be furnished with a rowid

    @log_db_changes(_log)
    def update_item(self, item):
        sql = """UPDATE items
                 SET category = ?, name = ?, price = ?
                 WHERE rowid = ?"""
        with self.conn as conn:
            conn.execute(
                        sql, 
                        self._to_values(item) + (item.rowid,)
                        )

    @log_db_changes(_log)
    def delete_item(self, item):
        sql = "DELETE FROM items WHERE rowid = ?"
        with self.conn as conn:
            conn.execute(
                        sql,
                        (item.rowid,)
                        )

    @log_db_items(_log)    
    def get_items(self):
        _sql = """SELECT rowid, category, name, price
                 FROM items"""
        with self.conn as conn:
            for row in conn.execute(_sql):
                item = DBItem(*row)
                yield item
                

class QuotesDB(): # Is this a bit overkill? Also doesn't really belong in Model?
    config = 'sqlite:///motivate/models/quotes.db'

    def __init__(self):
        self.conn = UseDatabase(self.config)

    def get_quote(self):
        _sql = '''SELECT quote FROM quotes  
                ORDER BY RANDOM()  
                LIMIT 1''' 
        with self.conn as conn:
            row = conn.execute(_sql)
            quote = row.fetchone()[0] 
        return quote
