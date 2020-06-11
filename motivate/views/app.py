# Standard library imports
import tkinter as tk
# Local application imports
from motivate.models.database import QuotesDB
from motivate.views.tkinter.pages import LoginPage, HomePage


class ViewLifecycle():
    def __init__(self, item_controller, money_controller):
        self._item_control = item_controller
        self._money_control = money_controller
        
    def start_app(self):
        TkView = TkViewManager()
        TkView.on('login-select', lambda index: self._item_control.select_item(index)) \
            .on('login-update', lambda item: self._item_control.update_item(item)) \
            .on('login-delete', lambda : self._item_control.delete_item()) \
            .on('login-save', lambda item: self._item_control.create_item(item)) \
            .on('login-next', lambda salary, price: self._money_control.load(salary, price)) \
            .on('home-start', lambda : self._money_control.start()) \
            .on('home-pause', lambda : self._money_control.pause_money()) \
            .on('home-reset', lambda : self._money_control.reset_money()) \
            .start(self._item_control.get_items())


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
                    self._render_home(float(item.price))
                    command(salary, float(item.price))
                self._commands['login-next'] = _next_internal
            else:
                self._commands[action] = command
            return self

        def start(self, items):   
            self._render_login(items)
            self._root.mainloop()

        def exit(self, name):
            self._notify(name)
            self._active_context.quit() # ?
            self._after_exit() # ?

        def _render_login(self, items):
            self._root.title("Settings")      
            self._active_context = LoginPage(self._root, self._commands, items)

        def _render_home(self, price):
            self._root.title("Progress")
            self._active_context = HomePage(self._root, price, self._commands)

        def _notify(self, name):
            mb.showinfo(
                        title='CONGRATULATIONS', 
                        message=f"Enjoy your {name}",
                        parent = self
                        )
