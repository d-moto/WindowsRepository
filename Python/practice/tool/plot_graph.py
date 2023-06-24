import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk

def plot_graph():
    function_type = function_var.get()
    a = float(a_entry.get())
    b = float(b_entry.get())
    c = float(c_entry.get())

    x = np.linspace(-10, 10, 400)

    if function_type == 'Quadratic':
        y = a*x**2 + b*x + c
        title = 'y = {}x^2 + {}x + {}'.format(a, b, c)
    elif function_type == 'Sine':
        y = a*np.sin(b*x + c)
        title = 'y = {}sin({}x + {})'.format(a, b, c)
    elif function_type == 'Fractional':
        y = a / (b*x + c)
        title = 'y = {} / ({}x + {})'.format(a, b, c)
    elif function_type == 'Exponential':
        y = a * np.exp(b*x) + c
        title = 'y = {}exp({}x) + {}'.format(a, b, c)
    elif function_type == 'Logarithmic':
        y = a * np.log(b*x) + c
        title = 'y = {}log({}x) + {}'.format(a, b, c)
    elif function_type == 'Composite':
        y = a * np.log(np.exp(b*x) + c)
        title = 'y = {}log(exp({}x) + {})'.format(a, b, c)

    fig = plt.figure()
    plt.plot(x, y)
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().grid(row=7, column=0, columnspan=4, pady=10)

root = tk.Tk()

style = ttk.Style()
style.theme_use('clam')

function_label = ttk.Label(root, text="Select function:")
function_label.grid(row=0, column=0, pady=10)
function_var = tk.StringVar(root)
function_var.set('Quadratic')  # default value
function_option = tk.OptionMenu(root, function_var, 'Quadratic', 'Sine', 'Fractional', 'Exponential', 'Logarithmic', 'Composite')
function_option.grid(row=0, column=1, pady=10)

a_label = ttk.Label(root, text="Enter a:")
a_label.grid(row=1, column=0, pady=10)
a_entry = ttk.Entry(root)
a_entry.grid(row=1, column=1, pady=10)

b_label = ttk.Label(root, text="Enter b:")
b_label.grid(row=2, column=0, pady=10)
b_entry = ttk.Entry(root)
b_entry.grid(row=2, column=1, pady=10)

c_label = ttk.Label(root, text="Enter c:")
c_label.grid(row=3, column=0, pady=10)
c_entry = ttk.Entry(root)
c_entry.grid(row=3, column=1, pady=10)

plot_button = ttk.Button(root, text="Plot", command=plot_graph
