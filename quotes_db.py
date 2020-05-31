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

quotes = ("\"I've failed over and over and over again in my life. And that is why I succeed.\" - Michael Jordan",
        "\"Think you can, think you can't; either way you'll be right.\" - Henry Ford",
        "\"An expert is a man who has made all the mistakes which can be made, in a very narrow field\" - Neils Bohr",
        "\"Everything you've ever wanted is on the other side of fear\" - George Addair")


_sql = 'INSERT INTO quotes VALUES (?)'
with UseDatabase() as conn:
    for quote in quotes:
        conn.execute(_sql, quote)
