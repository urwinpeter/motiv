import time
from motivate.models.database import ContactsDB

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
    def __init__(self, salary):
        self.earnings = Observable(0)
        self._rate = salary / (365 * 24 * 60 * 60)
        
    def addMoney(self, start_time):
        earnings = self._rate * (time.time() - start_time)
        self.earnings.val = (self.earnings.val + earnings)
        
    def resetMoney(self):
        self.earnings.val = 0

class LoginCalculator():
    def __init__(self):
        self.db = ContactsDB()
      
    def request_salary(self, contact):
        salary = self.db.get_salary(contact)
        print(salary)
        return salary
        
class RegisterCalculator():
    def __init__(self):
        self.db = ContactsDB()

    def addcontact(self, contact):
        self.db.add_contact(contact)
        print('DB success')

