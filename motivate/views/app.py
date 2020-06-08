import tkinter as tk
import tkinter.messagebox as mb
from motivate.views.formwidgets import EarningsForm, SalaryForm, ItemForm
from motivate.views.listwidgets import ItemList
from motivate.views.canvaswidgets import PieChart
from motivate.views.buttonwidgets import Button
from motivate.models.database import QuotesDB
from motivate.views.tkinter.home import HomePage
from motivate.views.tkinter.login import LoginPage


class ViewLifecycle():
    """
    The master component. Used to start/stop the app and delegate control 
    to controllers.

    ...

    Attributes
    ----------
    login_control : LoginController object
        Controls all events unique to the LoginPage
    home_control : HomeController object
        Controls all events unique to the HomePage
    """

    def __init__(self, home_controller, login_controller):
        self._home = home_controller
        self._login = login_controller

    def start_app(self):
        TkViewManager() \
            .on('login-update', lambda item: self._login.update(item)) \
            .on('login-delete', lambda item: self._login.delete(item)) \
            .on('login-save', lambda item: self._login.save(item)) \
            .on('login-next', lambda salary, item: self._home.load(salary, item)) \
            .on('home-start', lambda: self._home.start()) \
            .on('home-pause', lambda: self._home.pause_money()) \
            .on('home-reset', lambda: self._home.reset_money()) \
            .schedule(after=100, lambda)
            .start()
            
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
                    command(salary, item)
                    self._render_home(salary, item)
                self._commands['login-next'] = _next_internal
            else:
                self._commands[action] = command
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

        def _render_home(self, salary, ):
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
     