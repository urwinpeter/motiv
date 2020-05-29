import tkinter as tk 
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Pie(tk.Frame):
    explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. time left)
    colours = ['#0066CC','#DDDDDD']
    def __init__(self, master):
        super().__init__(master)
        self.fig = Figure(figsize=(2, 2), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
         
        self._pack()
        self.ax = self.fig.add_subplot()

    def _pack(self):
        self.pack()
        self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    
    def SetMoney(self, money):
        ratio = money/self.cost
        self.ax.clear()
        if ratio <=1:
            self.sizes = [ratio, 1-(ratio)]
        else: 
            self.sizes = [1, 0]
        self.ax.pie(self.sizes, explode=self.explode, colors = self.colours, autopct=None,
        shadow=False, startangle=90)
        self.fig.canvas.draw()

    def set_target(self, value):
        self.cost = value


    # def complete to make pie chart dissappear and replace with congratulations banner.


'''fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()'''


    
        

'''theta = np.arange(0., 2., 1./180.)*np.pi
fig = plt.figure(figsize=(6, 5), dpi=100)
ax = fig.add_subplot(111, projection='polar')
initial_n = 4
ax.plot(theta, 5*np.cos(initial_n*theta))
ax_s = plt.axes([0.15, 0.05, 0.25, 0.05])
slider_n = Slider(ax_s, '#of leaves', 3, 10, valinit=initial_n, 
                  valstep=1.0)

def onchanged(s_value):
    ax.clear()
    ax.plot(theta, 5*np.cos(int(s_value)*theta)) 

slider_n.on_changed(onchanged)


ebx = plt.axes([0.5, 0.005, 0.1, 0.05])
exit = Button(ebx, 'Quit')

def close(event):
    plt.close('all')

exit.on_clicked(close)

plt.show()'''