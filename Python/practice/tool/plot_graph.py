import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

def plot_graph():
    a = float(a_entry.get())
    b = float(b_entry.get())
    c = float(c_entry.get())

    x = np.linspace(-10, 10, 400)
    y = a*x**2 + b*x + c

    fig = plt.figure()
    plt.plot(x, y)
    plt.title('y = {}x^2 + {}x + {}'.format(a, b, c))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().grid(row=4, column=0, columnspan=4)

root = tk.Tk()

a_label = tk.Label(root, text="Enter a:")
a_label.grid(row=0, column=0)
a_entry = tk.Entry(root)
a_entry.grid(row=0, column=1)

b_label = tk.Label(root, text="Enter b:")
b_label.grid(row=1, column=0)
b_entry = tk.Entry(root)
b_entry.grid(row=1, column=1)

c_label = tk.Label(root, text="Enter c:")
c_label.grid(row=2, column=0)
c_entry = tk.Entry(root)
c_entry.grid(row=2, column=1)

plot_button = tk.Button(root, text="Plot", command=plot_graph)
plot_button.grid(row=3, column=0, columnspan=2)

close_button = tk.Button(root, text="Close", command=root.quit)
close_button.grid(row=5, column=0, columnspan=2)

root.mainloop()