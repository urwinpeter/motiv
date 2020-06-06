import tkinter as tk
import tkinter.messagebox as mb
from motivate.views.formwidgets import EarningsForm, SalaryForm, ItemForm
from motivate.views.listwidgets import ItemList
from motivate.views.canvaswidgets import PieChart
from motivate.views.buttonwidgets import Button
from motivate.models.database import QuotesDB

class ViewLifecycle():

    def __init__(self, home_controller, login_controller):
        self._home = home_controller
        self._login = login_controller

    def start_app(self):
        TkView() \
            .on('login-update', lambda item: self._login.update(item)) \
            .on('login-delete', lambda item: self._login.delete(item)) \
            .on('login-save', lambda item: self._login.save(item)) \
            .on('login-next', lambda salary, item: self._home.load(salary, item)) \
            .on('home-start', lambda: self._home.start()) \
            .on('home-pause', lambda: self._home.pause_money()) \
            .on('home-reset', lambda: self._home.reset_money()) \
            .start()

class TkView():
    
    def __init__(self):
        self._root = tk.Tk()
        self._commands = {}
        self._active_context = None
        self._root.geometry('800x350')
        self._after_exit = lambda: self._root.destroy

    def on(self, action, command):
        if(action == 'login-update'):
            self._commands['login-update'] = command
        elif(action == 'login-delete'):
            self._commands['login-delete'] = command
        elif(action == 'login-save'):
            self._commands['login-save'] = command
        elif(action == 'login-next'):
            def _next_internal(salary, item):
                command(salary, item)
                self._render_home(salary, item)
            self._commands['login-next'] = _next_internal
        elif(action == 'home-start'):
            self._commands['home-start'] = command
        elif(action == 'home-pause'):
            self._commands['home-pause'] = command
        elif(action == 'home-reset'):
            self._commands['home-reset'] = command
        return self

    def start(self):   
        self._root.mainloop()
        self._render_login()

    def exit(self, name):
        self._notify(name)
        self._active_context.quit()
        self._after_exit()

    def _render_login(self):
        self._root.title("Settings")
        self._active_context = LoginPage(self._root, self._commands)

    def _render_home(self, salary, item):
        price = float(item.price)
        quote = QuotesDB().get_quote()
        self._root.title("Progress")
        self._active_context = HomePage(self._root, price, quote, self._commands)

    def _notify(self, name):
        mb.showinfo(
                    title='CONGRATULATIONS', 
                    message=f"Enjoy your {name}",
                    parent = self
                    )

class LoginPage(tk.Frame):
    
    def __init__(self, root, commands):
        super().__init__(root)

        self.pack()
        ItemList(self).pack(side=tk.LEFT, padx=10, pady=10)
        ItemForm(self).pack(padx=10, pady=10)
        SalaryForm(self).pack(pady=10)
        self.next_button = Button(self, button_text='Next >')
        self.next_button.pack(side=tk.BOTTOM, pady=5)
        # self.item_listbox.bind_double_click(control.select_item)  
        self.item_form.bind_update(commands['login-update'])
        self.item_form.bind_delete(commands['login-delete'])
        self.item_form.bind_save(commands['login-save'])
        self.next_button.bind(commands['login-next'])

    def append_item(self, item):
        self.item_listbox.insert_item(item)

    def update_item(self, item, index):
        self.item_listbox.update_item(item, index)

    def remove_items(self):
        self.item_form.clear_entries()
        self.item_listbox.clear_items()

    def get_item_details(self):
        return self.item_form.get_item_details()

    def display_item_details(self, item):
        self.item_form.display_item_details(item)

    def get_salary(self):
        return self.salary_form.get_salary()


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

    def display_congrats(self, name):
        mb.showinfo(
                    title='CONGRATULATIONS', 
                    message=f"Enjoy your {name}",
                    parent = self
                    )
        
        