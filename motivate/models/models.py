import time
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

    def _notify(self, earnings, count) -> None:
        print("notifying observers..")
        for observer in self._observers:
            observer.update(earnings, count)

    @property
    def val(self):
        return self._val

    @val.setter
    def val(self, value):
        self._val1 = value
        self._notify(self._val1)
        
class Calculator():
    def __init__(self, *args):
        self.obs = [Observable(value) for value in args]
        
class HomeCalculator(Calculator)
    def __init__(self):
        super().__init__(0, True) 
        salary = 1_000_000
        self.earnings = self.obs[0] 
        self.count = self.obs[1]
        self._rate = salary / (365 * 24 * 60 * 60)
        self._start_time = time.time()
    
    def addMoney(self):
        earnings = self._rate * (time.time() - self._start_time)
        self.earnings = (self.earnings + earnings)
            
    def pauseMoney(self):
        self.count = False
        
    def resetMoney(self):
        self.count = None
        self.earnings = 0

class LoginCalculator(Calculator):
    def __init__(self):
        super().__init__('Alan@b.com', 'pass')
        self.user = self.obs[0]
        self.pass_ = self.obs[1]
        
    def check(self, username, password):
        if self.user == username and self.pass_ == password:
            return True    

class RegisterCalculator():
    def __init__(self):
        #self.obs = Observable()
        self.db = ContactsDB()

    def addcontact(self, contact):
        self.db.add_contact(contact)
        print('success')

