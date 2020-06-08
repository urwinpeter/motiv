
class MoneyService:

    def __init__(self):
        self._calculator = EarningsCalculator(salary, price)
        self.calculator.attach(observer=self)

    def start_calc(self, salary, item):
        price = float(item.price)
        quote = QuotesDB().get_quote()        
        self._counting_status = False
        self.update_earnings(0)
        
    def start(self, event=None):
        self._start_time = time.time()
        self._add_money(self._start_time)
        
    def _add_money(self, time):
        self._counting_status = True
        (amount, complete) = self.calculator.add_money(time)
        if complete:
            self.home_view.update_earnings(amount)
            view.exit(self.item.name)
        else:
            self.home_view.update_status(self._counting_status)

    def pause_money(self, event=None):
        self._counting_status = False

    def reset_money(self, event=None):
        self._counting_status = None
        self.calculator.reset_money()
        self.home_view.update_status(self._counting_status)

    def update_earnings(self, money):
        self.home_view.update_earnings(money)
        self.home_view.after(100, 
                            lambda : self._add_money(self._start_time) 
                            if self._counting_status == True  
                            else None
                            ) # or use observer.attach/detach in pausemoney/resetmoney etc
