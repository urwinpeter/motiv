import time

class Observable():
    def __init__(self, value, target):
        self._observers = []
        self._val = value
        self._target = target

    def attach(self, observer) -> None:
        print("attached observer " + str(observer))
        self._observers.append(observer)

    def detach(self, observer) -> None:
        self._observers.remove(observer)

    def _notify_update(self, value) -> None:
        print("notifying observers..")
        for observer in self._observers:
                observer.update_earnings(value)

    def _notify_complete(self):
        for observer in self._observers:
            observer.mission_accomplished(self._target)
        
    @property
    def val(self):
        return self._val

    @val.setter
    def val(self, value):
        if value <= self._target:
            self._val = value
            self._notify_update(self._val)
        else:
            self._notify_complete()
        
class EarningsCalculator():
    def __init__(self, salary, target):
        self.earnings = Observable(0, target)
        self._rate = salary / (365 * 24 * 60 * 60)
         
    def add_money(self, start_time):
        earnings = self._rate * (time.time() - start_time)
        self.earnings.val  = self.earnings.val + earnings
        
    def reset_money(self):
        self.earnings.val = 0
    
    def attach(self, observer):
        self.earnings.attach(observer)
