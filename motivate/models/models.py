import time
from motivate.models.database import QuotesDB

class Observable():
    def __init__(self, value, item):
        self._observers = []
        self._val = value
        self._target = float(item.price) 

    def attach(self, observer) -> None:
        print("attached observer " + str(observer))
        self._observers.append(observer)

    def detach(self, observer) -> None:
        self._observers.remove(observer)

    def _notify_update(self, value) -> None:
        print("notifying observers..")
        for observer in self._observers:
                observer.update(value)

    def _notify_complete(self):
        for observer in self._observers:
            observer.mission_accomplished(self._target)
        
    @property
    def val(self):
        return self._val

    @val.setter
    def val(self, value):
        if value <= self._target: ## could turn this into decorator # make it so it takes into account the incremental increase every time interavaal
            self._val = value
            self._notify_update(self._val)
        else:
            self._notify_complete()
        
class HomeCalculator():
    def __init__(self, salary, item):
        self.db = QuotesDB()
        self.earnings = Observable(0, item)
        self._rate = salary / (365 * 24 * 60 * 60)
         
    def addMoney(self, start_time):
        earnings = self._rate * (time.time() - start_time)
        self.earnings.val  = self.earnings.val + earnings
        
    def resetMoney(self):
        self.earnings.val = 0

    def get_quote(self):
        return self.db.get_quote()


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

