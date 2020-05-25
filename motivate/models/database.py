import sqlalchemy as sa

class UseDatabase:
    """Context manager to manage connection with database"""
    def __init__(self):
        pass

    def __enter__(self):
        db_config = 'ibm_db_sa://vtj92335:g273jnvdb8jxm%2B5n@dashdb-txn-sbox-yp-lon02-01.services.eu-gb.bluemix.net:50000/BLUDB'
        self.engine = sa.create_engine(db_config)
        self.conn = self.engine.connect() 
        return self.conn
        
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.conn.close()


class ContactsDB(object):
    def __init__(self):
        pass

    def to_values(self, c):
        return c.last_name, c.first_name, c.email, c.phone

    def get_salary(self, name):
        _sql = f"""SELECT  salary
                 FROM users
                 WHERE username = {name}"""
        with UseDatabase() as conn:
            proxy = conn.execute(_sql)
            salary = proxy.fetchone()
            return salary
    
    def add_contact(self, contact):
        _sql = f"""INSERT INTO users VALUES
                ('{contact.username}', 
                '{contact.password}', 
                '{contact.salary}')"""
        with UseDatabase() as conn:
            conn.execute(_sql)
        #except user already exists

    def update_contact(self, contact):
        rowid = contact.rowid
        sql = """UPDATE contacts
                 SET last_name = ?, first_name = ?, email = ?, 
                 phone = ?
                 WHERE rowid = ?"""
        with self.conn:
            self.conn.execute(sql, self.to_values(contact) + (rowid,))
        return contact

    def delete_contact(self, contact):
        sql = "DELETE FROM contacts WHERE rowid = ?"
        with self.conn:
            self.conn.execute(sql, (contact.rowid,))