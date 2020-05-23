import time

class Observable():
    def __init__(self):
        self._earnings = 0
        self._count = True
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
    def earnings(self):
        return self._earnings

    @earnings.setter
    def earnings(self, earnings):
        self._earnings = earnings
        self._notify(self._earnings, self._count)

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, count):
        self._count = count
        
class Calculator():
    def __init__(self):
        salary = 1_000_000
        self.obs = Observable()
        self._rate = salary / (365 * 24 * 60 * 60)
        self._start_time = time.time()
        
    def addMoney(self):
        earnings = self._rate * (time.time() - self._start_time)
        self.obs.earnings = (self.obs.earnings + earnings)
            
    def pauseMoney(self):
        self.obs.count = False
        
    def resetMoney(self):
        self.obs.count = None
        self.obs.earnings = 0
