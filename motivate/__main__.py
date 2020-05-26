import tkinter as tk
from motivate.controllers.controller import LoginController
from motivate.models.models import LoginCalculator
from motivate.views.widgets import Form, LoginEventWidget

def main():
    root = tk.Tk()
    root.geometry('500x500')
    root.title("Let's Get Pumped!")

    fields = ["Username", "Password"]
    states = ({'text':'Submit'},
            {'text':'Register', 'fg':'red', 'relief':'flat'}
                  )
    model = LoginCalculator()              
    view1 = Form(root, fields)
    view2 = LoginEventWidget(view1, states)
    app = LoginController(root, model, view1, view2)
    
    root.mainloop()

if __name__ == "__main__":
    main()
