import tkinter as tk
from motivate.views.tkinter.formwidgets import EarningsForm, SalaryForm, ItemForm
from motivate.views.tkinter.listwidgets import ItemList
from motivate.views.tkinter.canvaswidgets import PieChart
from motivate.views.tkinter.buttonwidgets import Button
from pubsub import pub

class LoginPage(tk.Frame):
    def __init__(self, root, commands):
        super().__init__(root)
        # Subscribe to Updates
        pub.subscribe(self.update_items, "item_changed")
        # Create Widgets
        self.item_listbox = ItemList(self)
        self.item_form = ItemForm(self)
        self.salary_form = SalaryForm(self)
        self.next_button = Button(self, button_text='Next >')
        # Pack Widgets
        self.pack() 
        self.item_listbox.pack(side=tk.LEFT, padx=10, pady=10)
        self.item_form.pack(padx=10, pady=10)
        self.salary_form.pack(pady=10)
        self.next_button.pack(side=tk.BOTTOM, pady=5)
        # Bind Callbacks
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

    def update_items(self, items, selected_item):
        self._remove_items()
        self._load_items(items, selected_item)

    def _remove_items(self):
        self.item_form.clear_entries()
        self.item_listbox.clear_items()
    
    def _load_items(self, items, selected_item):
        for item in items:
            self.item_listbox.insert_item(item)
        self.item_form.display_item_details(selected_item)


class HomePage(tk.Frame):
    def __init__(self, root, price, quote, commands):
        super().__init__(root)
        # Subscribe to Updates
        pub.subscribe(self.update_earnings, "money_changed")
        # Create and Pack Widgets
        self.earnings_form = EarningsForm(
                            item_price=price, 
                            master_widget=self
                            )
        tk.Message(
                master=self, 
                text = quote, 
                width=300, 
                justify =tk.CENTER, 
                font = ("Helvetica", 16, "bold italic")
                ).pack()
        self.piechart = PieChart(self, price)
        self.pack()
        self.earnings_form.pack()
        self.piechart.pack()
        # Bind Callbacks
        self.earnings_form.bind_start(commands['home-start'])
        self.earnings_form.bind_pause(commands['home-pause'])
        self.earnings_form.bind_reset(commands['home-reset'])

    def update_earnings(self, money):  
        self.earnings_form.update_earnings(money)
        self.piechart.update_chart(money)
