import sqlalchemy as sa
from motivate.item import Item

class UseDatabase:
    """Context manager to manage connection with database"""
    def __init__(self, config):
        self.engine = sa.create_engine(config)

    def __enter__(self):
        self.conn = self.engine.connect() 
        return self.conn
        
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.conn.close()

class ItemsDB():
    db_config = 'ibm_db_sa://vtj92335:g273jnvdb8jxm%2B5n@dashdb-txn-sbox-yp-lon02-01.services.eu-gb.bluemix.net:50000/BLUDB'
    def __init__(self):
        self.conn = UseDatabase(self.db_config)

    def add_item(self, item):
        _sql = f"""INSERT INTO users VALUES
                ('{item.category}', 
                '{item.name}', 
                '{item.cost}')"""
        with self.conn as conn:
            conn.execute(_sql)
        #except user already exists

    def get_items(self):
        _sql = """SELECT rowid, username, password, salary
                 FROM users"""
        with self.conn as conn:
            for row in conn.execute(_sql):
                item = Item(*row[1:])
                item.rowid = row[0]
                yield item

    def update_item(self, item):
        sql = """UPDATE items
                 SET last_name = ?, first_name = ?, email = ?, phone = ?
                 WHERE rowid = ?"""
        with self.conn as conn:
            conn.execute(sql, self.to_values(item) + (item.rowid,))
        #return item

    def delete_item(self, item):
        sql = "DELETE FROM items WHERE rowid = ?"
        with self.conn as conn:
            conn.execute(sql, (item.rowid,))

class QuotesDB():
    db_config = 3
    def __init__(self):
        self.conn = UseDatabase(self.db_config)

    def get_quote(self):
        _sql = '''SELECT quote FROM quotes  
                ORDER BY RAND ( )  
                LIMIT 1''' 
        with self.conn as conn:
            quote = conn.execute(_sql)[0]
            return quote

        



    '''def get_cost(self, item):
        _sql = f"""SELECT  cost
                 FROM users
                 WHERE username = '{item.category}'
                 AND password = '{item.name}' """
        with self.conn as conn:
            proxy = conn.execute(_sql)
            cost = proxy.fetchone()
            return cost'''
    