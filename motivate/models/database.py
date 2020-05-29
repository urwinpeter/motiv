import sqlalchemy as sa
from motivate.item import Item

class UseDatabase:
    """Context manager to manage connection with database"""
    def __init__(self, db_config):
        self.engine = sa.create_engine(db_config)

    def __enter__(self):
        self.conn = self.engine.connect() 
        return self.conn
        
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.conn.close()

class ItemsDB():
    config = 'ibm_db_sa://vtj92335:g273jnvdb8jxm%2B5n@dashdb-txn-sbox-yp-lon02-01.services.eu-gb.bluemix.net:50000/BLUDB'
    def __init__(self):
        self.conn = UseDatabase(self.config)

    def _to_values(self, c):
        return c.category, c.name, c.price

    def add_item(self, item):
        _sql = f"""INSERT INTO items VALUES
                (?, ?, ?)"""
        with self.conn as conn:
            rowid = conn.execute(_sql,
                                self._to_values
                                ).lastrowid
            item.rowid = rowid
        return item
        
    def get_items(self):
        _sql = """SELECT rowid, category, name, price
                 FROM items"""
        with self.conn as conn:
            for row in conn.execute(_sql):
                item = Item(*row[1:])
                item.rowid = row[0]
                yield item

    def update_item(self, item):
        sql = """UPDATE items
                 SET category = ?, name = ?, price = ?
                 WHERE rowid = ?"""
        with self.conn as conn:
            conn.execute(sql, self._to_values(item) + (item.rowid))
        # return item

    def delete_item(self, item):
        sql = "DELETE FROM items WHERE rowid = ?"
        with self.conn as conn:
            conn.execute(sql, (item.rowid))

class QuotesDB():
    config = 3
    def __init__(self):
        self.conn = UseDatabase(self.config)

    def get_quote(self):
        _sql = '''SELECT quote FROM quotes  
                ORDER BY RAND ( )  
                LIMIT 1''' 
        with self.conn as conn:
            quote = conn.execute(_sql)[0]
        return quote
