# Standard library imports
import threading
import time
# Third party imports
from pubsub import pub
# Local application imports
from motivate.models.calculator import EarningsCalculator


class MoneyService():
    def __init__(self):
        self.calculator = EarningsCalculator()
        self._counting_status = True
        self._target = 0
        self._earnings = 0
        self._start_time = 0
    
    def start(self):
        self._start_time = time.time()
        self._counting_status = True
        self._add_money()
        
    def add_money(self):
        if not self._start_time:
            self._start_time = time.time()
        if self._counting_status:
            self.earnings = self.calculator.add_money(self._start_time)
        #threading.Timer(1, self._add_money).start()

    def pause_money(self):
        self._counting_status = False
    
    def reset_money(self):
        self._counting_status = False
        self.calculator.reset_money()

    def set_user_values(self, salary, price):
        self._target = price
        self.calculator.set_user_rate(
            salary / (365 * 24 * 60 * 60)
            )

    def set_initial_earnings(self):
        self.earnings = 0  # This is here to trigger view being updated with initial earnings of 0. Does it really belong here?

    @property
    def earnings(self):
        return self._earnings

    @earnings.setter
    def earnings(self, value):
        if value <= self._target:
            self._earnings = value
            pub.sendMessage("money_changed", money=value)
        else:
            self._earnings = self._target
            pub.sendMessage("target_reached", money=self._target)
