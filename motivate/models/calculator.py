import time

class Observable():
    def __init__(self, value):
        self._observers = []
        self._value = value

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
    def value(self):
        if value <= self._target:
            return self._value
        else:
            self._notify_complete()

    @value.setter
    def value(self, value):
        self._value = value
       
        
class EarningsCalculator():
    def __init__(self, salary, target):
        self.earnings = Observable(0)
        self._rate = salary / (365 * 24 * 60 * 60)
        self._target = target
         
    def add_money(self, start_time):
        earnings = self._rate * (time.time() - start_time)
        self.earnings.value  = self.earnings.value + earnings
        if self.earnings.value <= self._target:
            return self._value, False,
        else:
            return self._target, True,
        
    def reset_money(self):
        self.earnings.value = 0
    
    def attach(self, observer):
        self.earnings.attach(observer)
