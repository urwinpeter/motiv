# Standard library imports
import tkinter as tk
# Third party imports
from pubsub import pub
# Local application imports
from motivate.views.tkinter.buttonwidgets import Button
from motivate.views.tkinter.canvaswidgets import PieChart
from motivate.views.tkinter.formwidgets import EarningsForm, SalaryForm, ItemForm
from motivate.views.tkinter.listwidgets import ItemList


class LoginPage(tk.Frame):
    def __init__(self, root, commands, items):
        super().__init__(root)
        # Subscribe to updates
        pub.subscribe(self.select_item, "item_selected")
        # Create widgets
        self.item_listbox = ItemList(self, items)
        self.item_form = ItemForm(self)
        self.salary_form = SalaryForm(self)
        self.next_button = Button(self, button_text='Next >')
        # Pack widgets
        self.pack()
        self.item_listbox.pack(side=tk.LEFT, padx=10, pady=10)
        self.item_form.pack(padx=10, pady=10)
        self.salary_form.pack(pady=10)
        self.next_button.pack(side=tk.BOTTOM, pady=5)
        # Bind callbacks
        self.item_listbox.bind_double_click(commands['login-select'])
        self.item_form.bind_update(commands['login-update'])
        self.item_form.bind_delete(commands['login-delete'])
        self.item_form.bind_save(commands['login-save'])
        self.bind_next(commands['login-next'])

    def bind_next(self, callback):
        def _callback(event=None):
            item = self.item_form.get_item_details()
            salary = self.salary_form.get_salary()
            if item and salary:
                self.destroy()
                callback(salary, item)
        self.next_button.bind(_callback)

    def save_item(self, item):
        self.item_listbox.insert_item(item)

    def update_item(self, item):
        self.item_listbox.update_item(item)

    def delete_item(self):
        self.item_listbox.delete_item()

    def select_item(self, item):
        self.item_form.display_item_details(item)


class HomePage(tk.Frame):
    def __init__(self, root, price, commands):
        super().__init__(root)
        # Subscribe to updates
        pub.subscribe(self.update_earnings, "money_changed")
        pub.subscribe(self.load_quote_text, "quote_ready")
        # Create and pack widgets
        self.earnings_form = EarningsForm(
            item_price=price,
            master_widget=self
            )
        self.quote = tk.Message(
            master=self, width=300,
            justify=tk.CENTER, font=("Helvetica", 16, "bold italic")
            )
        self.piechart = PieChart(self, price)
        self.pack()
        self.quote.pack()
        self.earnings_form.pack()
        self.piechart.pack()
        # Bind callbacks
        self.earnings_form.bind_start(commands['home-start'])
        self.earnings_form.bind_pause(commands['home-pause'])
        self.earnings_form.bind_reset(commands['home-reset'])

    def update_earnings(self, money):
        self.earnings_form.update_earnings(money)
        self.piechart.update_chart(money)

    def load_quote_text(self, quote):
        self.quote.config(text=quote)
