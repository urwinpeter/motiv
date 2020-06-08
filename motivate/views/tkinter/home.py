
class HomePage(tk.Frame):
    
    def __init__(self, root, quote, price, commands):
        super().__init__(root)
        self.earnings_form = EarningsForm(
                            item_price=price, 
                            master_widget=self
                            )
        self.quote = tk.Message(
                                master=self, 
                                text = quote, 
                                width=300, 
                                justify =tk.CENTER, 
                                font = ("Helvetica", 16, "bold italic")
                                )
        self.piechart = PieChart(self, price)
        self.pack()
        self.quote.pack()
        self.earnings_form.pack()
        self.piechart.pack()
        self.earnings_form.bind_start(commands['home-start'].start)
        self.earnings_form.bind_pause(commands['home-pause'].pause_money)
        self.earnings_form.bind_reset(commands['home-reset'].reset_money)

    def update_earnings(self, money):
        self.earnings_form.update_earnings(money)
        self.piechart.update_chart(money)
        
    def update_status(self, count):
        self.earnings_form.update_button_status(count)