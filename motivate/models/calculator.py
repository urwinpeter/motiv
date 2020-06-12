# Standard library imports
import time


class EarningsCalculator():
    def __init__(self):
        self._rate = 0
        self.earnings = 0
          
    def add_money(self, start_time):
        earnings = self._rate * (time.time() - start_time)
        self.earnings = self.earnings + earnings
        return self.earnings
        
    def reset_money(self):
        self.earnings = 0
    
    def set_user_rate(self, rate):
        self._rate = rate

