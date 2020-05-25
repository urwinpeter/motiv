import time
from motivate.models.database import ContactsDB
'''The inheritance in this module is currently pretty pointless...e.g. in Homcalculator 
would be easier to just assign earning and count directly as opposed to via the super()
constructor'''

class Observable():
    def __init__(self, value):
        self._val = value
        self._observers = []

    def attach(self, observer) -> None:
        print("attached observer " + str(observer))
        self._observers.append(observer)

    def detach(self, observer) -> None:
        self._observers.remove(observer)

    def _notify(self, value) -> None:
        print("notifying observers..")
        for observer in self._observers:
            observer.update(value)

    @property
    def val(self):
        return self._val

    @val.setter
    def val(self, value):
        self._val1 = value
        self._notify(self._val1)
        
class HomeCalculator():
    def __init__(self):
        salary = 1_000_000
        self.earnings = Observable(0)
        self._rate = salary / (365 * 24 * 60 * 60)
        self._start_time = time.time()
    
    def addMoney(self):
        earnings = self._rate * (time.time() - self._start_time)
        self.earnings.val = (self.earnings.val + earnings)
        
    def resetMoney(self):
        self.earnings.val = 0

class LoginCalculator():
    def __init__(self):
        self.user = Observable('Alan@b.com')
        self.pass_ = Observable('pass')
        
    def check(self, contact):
        print(self.user.val, self.pass_.val)
        if self.user.val == contact.username and self.pass_.val == contact.password:
            return True    

class RegisterCalculator():
    def __init__(self):
        self.db = ContactsDB()

    def addcontact(self, contact):
        self.db.add_contact(contact)
        print('success')

