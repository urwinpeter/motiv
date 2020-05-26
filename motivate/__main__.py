import tkinter as tk
from motivate.controllers.controller import LoginController
from motivate.models.models import LoginCalculator
from motivate.views.widgets import Form, EventWidget

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
    view2 = EventWidget(view1, states)
    app = LoginController(root, model, view1, view2)
    commands = [app.Submit, 
                app.Register]
    view2.set_ctrl(commands)

    root.mainloop()

if __name__ == "__main__":
    main()
