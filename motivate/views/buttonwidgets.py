import tkinter as tk

class Button(tk.Button):
    def __init__(self, master_widget, button_text):
        super().__init__(
                master=master_widget, 
                text=button_text,
                activeforeground='blue' 
                )

    def bind(self, callback):
        super().bind('<Return>', callback)
        self.config(command=callback)
        
