import tkinter as tk
import tkinter.messagebox as mb
from motivate.views.formwidgets import EarningsForm, SalaryForm, ItemForm
from motivate.views.listwidgets import ItemList
from motivate.views.canvaswidgets import PieChart
from motivate.views.buttonwidgets import Button
from motivate.models.database import ItemsDB, QuotesDB

class TkViewManager():
        def __init__(self):
            self._root = tk.Tk()
            self._commands = {}
            self._active_context = None
            self._root.geometry('800x350')
            self._after_exit = lambda: self._root.destroy

        def on(self, action, command): 
            if(action == 'login-next'):
                def _next_internal(salary, item):
                    self._render_home(salary, item)
                    command(salary, item.price)
                self._commands['login-next'] = _next_internal
            else:
                def _command(*args):
                    command(*args, self._active_context)
                self._commands[action] = _command
            return self

        def start(self):   
            self._render_login()
            self._root.mainloop()

        def exit(self, name):
            self._notify(name)
            self._active_context.quit() # ?
            self._after_exit() # ?

        def _render_login(self):
            self._root.title("Settings")      
            items = list(ItemsDB().get_items())
            self._active_context = LoginPage(self._root, self._commands, items)

        def _render_home(self, salary, item):
            price = float(item.price) 
            quote = QuotesDB().get_quote() # Here or in Homepage?
            self._root.title("Progress")
            self._active_context = HomePage(self._root, price, quote, self._commands)

        def _notify(self, name):
            mb.showinfo(
                        title='CONGRATULATIONS', 
                        message=f"Enjoy your {name}",
                        parent = self
                        )


class ViewLifecycle():
    def __init__(self, login_controller, home_controller):
        self._home = home_controller
        self._login = login_controller

    def start_app(self):
        TkView = TkViewManager()
        TkView.on('login-select', lambda index, con: self._login.select_item(index, con))
        TkView.on('login-update', lambda item, con: self._login.update_item(item, con)) 
        TkView.on('login-delete', lambda con: self._login.delete_item(con)) 
        TkView.on('login-save', lambda item, con: self._login.create_item(item, con)) 
        TkView.on('login-next', lambda salary, price: self._home.load(salary, float(price))) 
        TkView.on('home-start', lambda con: self._home.start(con)) 
        TkView.on('home-pause', lambda con: self._home.pause_money(con)) 
        TkView.on('home-reset', lambda con: self._home.reset_money(con))
        #TkView.schedule(after=100, lambda)
        TkView.start()
            

class LoginPage(tk.Frame):
    def __init__(self, root, commands, items):
        super().__init__(root)
        self.item_listbox = ItemList(self)
        self.item_form = ItemForm(self)
        self.salary_form = SalaryForm(self)
        self.next_button = Button(self, button_text='Next >')
        self._pack() 
        for item in items:
            self.append_item(item)
        
        self.item_listbox.bind_double_click(commands['login-select'])
        self.item_form.bind_update(commands['login-update'])
        self.item_form.bind_delete(commands['login-delete'])
        self.item_form.bind_save(commands['login-save'])
        self.bind_next(commands['login-next'])

    def _pack(self):
        self.pack() # Pack Login Page Inside Tk 
        # Pack the remaining widgets inside Login Page
        self.item_listbox.pack(side=tk.LEFT, padx=10, pady=10)
        self.item_form.pack(padx=10, pady=10)
        self.salary_form.pack(pady=10)
        self.next_button.pack(side=tk.BOTTOM, pady=5)
        self.item=None
        self.salary=None
        
    def bind_next(self, callback):
        def _callback(event=None):
            item = self.get_item_details()
            salary = self.get_salary()
            if item and salary:
                self.destroy()
                callback(salary, item)
        self.next_button.bind(_callback)

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
    def __init__(self, root, price, quote, commands):
        super().__init__(root)
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

        self.earnings_form.bind_start(commands['home-start'])
        self.earnings_form.bind_pause(commands['home-pause'])
        self.earnings_form.bind_reset(commands['home-reset'])

    def update_earnings(self, money):    # This Can't be called from current place in controllers which doesn't see view
        self.earnings_form.update_earnings(money)
        self.piechart.update_chart(money)

    #self.home_view.display_congrats(self.item.name)