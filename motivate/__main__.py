import tkinter as tk
#from motivate.controllers.home(controller) import Controller
from motivate.controllers.login import Controller

def main():
    root = tk.Tk()
    root.geometry('500x500')
    root.title("Let's Get Pumped!")
    app = Controller(root)
    root.mainloop()

if __name__ == "__main__":
    main()
