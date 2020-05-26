import sqlalchemy as sa

class UseDatabase:
    """Context manager to manage connection with database"""
    def __init__(self):
        db_config = 'ibm_db_sa://vtj92335:g273jnvdb8jxm%2B5n@dashdb-txn-sbox-yp-lon02-01.services.eu-gb.bluemix.net:50000/BLUDB'
        self.engine = sa.create_engine(db_config)

    def __enter__(self):
        self.conn = self.engine.connect() 
        return self.conn
        
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.conn.close()

class ContactsDB(object):
    def __init__(self):
        self.conn = UseDatabase()

    def get_salary(self, contact):
        _sql = f"""SELECT  salary
                 FROM users
                 WHERE username = '{contact.username}'
                 AND password = '{contact.password}' """
        with self.conn as conn:
            proxy = conn.execute(_sql)
            salary = proxy.fetchone()
            return salary
    
    def add_contact(self, contact):
        _sql = f"""INSERT INTO users VALUES
                ('{contact.username}', 
                '{contact.password}', 
                '{contact.salary}')"""
        with self.conn as conn:
            conn.execute(_sql)
        #except user already exists
