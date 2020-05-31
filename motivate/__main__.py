import tkinter as tk
import locale
from motivate.controllers.controller import LoginController
from motivate.models.database import ItemsDB
from motivate.views.pages import LoginPage

locale.setlocale(locale.LC_ALL, '')

def main():
    PageController().start_login()

if __name__ == "__main__":
    main()


'''root = tk.Tk()

home = HomeController(root)
login = LoginController(root, home)'''
