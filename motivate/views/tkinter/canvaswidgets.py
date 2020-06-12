# Standard library imports
import tkinter as tk
# Third party imports
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class PieChart(tk.Frame):
    def __init__(self, master, item_price):
        super().__init__(master)
        self.item_price = item_price
        self.fig = Figure(figsize=(2, 2), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self._pack()
        self.axes = self.fig.add_subplot()

    def _pack(self):
        self.pack()
        self.canvas._tkcanvas.pack(
            side=tk.TOP,
            fill=tk.BOTH,
            expand=1
            )

    def update_chart(self, money):
        ratio = money/self.item_price
        self.axes.clear()
        wedge_sizes = [ratio, 1-(ratio)]
        self.axes.pie(
            wedge_sizes,
            colors=['#0066CC', '#DDDDDD'],
            autopct=None,
            shadow=False,
            startangle=90
            )
        self.fig.canvas.draw()
