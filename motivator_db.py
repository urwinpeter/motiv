import sqlalchemy as sa 

class UseDatabase():
    """Context manager to manage connection with database"""
    def __init__(self):
        self.engine = sa.create_engine('sqlite:///motivate.db')

    def __enter__(self):
        self.conn = self.engine.connect() 
        return self.conn
        
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.conn.close()

_sql = '''CREATE TABLE items
        (category varchar(255),
        name varchar(255),
        price float()'''

with UseDatabase() as conn:
    conn.execute(_sql)

items = {'Shoes':(('Running Shoes',100),
                 ('Football Boots', 150),
                 ('Trainers', 45)),
        'Electronics': (('iPhone', 600),
                ('Laptop', 1000),
                ('HeadPhones', 30)),
        'Activities': (('Date Night', 70),
                ('Cinema', 30),
                ('Paintballing', 90)),
        'Holidays':(('Weekend Escape', 300),
                ('Family Holiday', 2000),
                ('Honeymoon', 5000))}

_sql = 'INSERT INTO items VALUES (?,?,?)'
with UseDatabase() as conn:
    for key, values in items:
            conn.execute(_sql, key, value[0], value[1])
