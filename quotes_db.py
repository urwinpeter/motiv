import sqlalchemy as sa 

class UseDatabase():
    """Context manager to manage connection with database"""
    def __init__(self):
        self.engine = sa.create_engine('sqlite:///quotes.db')

    def __enter__(self):
        self.conn = self.engine.connect() 
        return self.conn
        
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.conn.close()

_sql = "DROP TABLE quotes"

with UseDatabase() as conn:
    conn.execute(_sql)

_sql = '''CREATE TABLE quotes
        (quote TEXT(255)
        )'''

with UseDatabase() as conn:
    conn.execute(_sql)

quotes = ("Don't be limited by someone else's limited imagination",
        "Whether you say 'I can' or 'I can not', you are right either way",
        "An expert is a man who has made all the mistakes which can be made, in a very narrow field",
        "Everything you desire is on the other side of fear")


_sql = 'INSERT INTO quotes VALUES (?)'
with UseDatabase() as conn:
    for quote in quotes:
        conn.execute(_sql, quote)
