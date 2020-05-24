import tkinter as tk
from motivate.controllers.controller import LoginController
from motivate.models.models import LoginCalculator
from motivate.views.views import Form, EventWidget

def main():
    root = tk.Tk()
    root.geometry('500x500')
    root.title("Let's Get Pumped!")
    app = LoginController(root, start_login())
    root.mainloop()

if __name__ == "__main__":
    main()
