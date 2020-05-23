from motivate.contact import Contact
from motivate.models.database import ContactsDB

class Observable():
    
    def __init__(self):
        self._user = 'Alan@b.com'
        self._pass = 'pass'
        self._observers = []

    @property
    def username(self):
        return self._user

    @username.setter
    def username(self, usernam):
        self._user = username
        self._notify(self._user)

    @property
    def password(self):
        return self._pass

    @password.setter
    def password(self, pass_):
        self._pass = pass_
        
class Calculator():
    def __init__(self):
        #self.obs = Observable()
        self.db = ContactsDB()

    def addcontact(self, details):
        self.contact = Contact(*details)
        #except invalid formats
        self.db.add_contact(*details)
        print('success')
