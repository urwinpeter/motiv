import tkinter as tk
from motivate.controller import Controller

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('500x500')
    root.title("Let's Get Pumped!")
    app = Controller(root)
    root.mainloop()