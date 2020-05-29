import time
from motivate.models.database import ItemsDB

class Observable():
    def __init__(self, value):
        self._val = value
        self._observers = []
        self._target = 0 # do i need this line

    def attach(self, observer) -> None:
        print("attached observer " + str(observer))
        self._observers.append(observer)

    def detach(self, observer) -> None:
        self._observers.remove(observer)

    def _val_notify(self, value) -> None:
        print("notifying observers..")
        for observer in self._observers:
                observer.update(value)
        if self.val >= self.target: ## could turn this into decorator # make it so it takes into account the incremental increase every time interavaal
            print('SUCCCESSS')
            observer.PauseMoney()
            observer.complete()
        
    def _target_notify(self, value):
        print('target')
        print(value, type(value))
        for observer in self._observers:
            observer.set_target(value)

    @property
    def val(self):
        return self._val

    @val.setter
    def val(self, value):
        self._val = value
        self._val_notify(self._val)

    @property
    def target(self):
        return self._target

    @target.setter
    def target(self, value):
        self._target = value
        self._target_notify(self._target)
        
class HomeCalculator():
    def __init__(self, salary):
        self.db = ItemsDB()
        self.earnings = Observable(0)
        self._rate = salary / (365 * 24 * 60 * 60)
 
    def addMoney(self, start_time):
        earnings = self._rate * (time.time() - start_time)
        self.earnings.val = (self.earnings.val + earnings)
        
    def resetMoney(self):
        self.earnings.val = 0

    def get_quote(self):
        return self.db.get_quote()

    def set_target(self, target):
        self.earnings.target = target

class LoginCalculator():
    def __init__(self):
        self.db = ContactsDB()
      
    def request_salary(self, contact):
        salary = self.db.get_salary(contact)
        print(salary)
        return salary

    def get_items(self):
        return self.db.get_contacts()
        
class RegisterCalculator():
    def __init__(self):
        self.db = ContactsDB()

    def addcontact(self, contact):
        self.db.add_contact(contact)
        print('DB success')

