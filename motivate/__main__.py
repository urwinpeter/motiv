import tkinter as tk
import locale
from motivate.controllers.controller import LoginController
from motivate.models.database import ItemsDB
from motivate.views.pages import LoginPage

locale.setlocale(locale.LC_ALL, '')

def main():
    locale.setlocale(locale.LC_ALL, '')
    root = tk.Tk()

    model = ItemsDB()              
    view = LoginPage(root)
    app = LoginController(root, model, view)
    
    root.mainloop()

if __name__ == "__main__":
    main()
