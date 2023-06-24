import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk

class GUIApp:
    def __init__(self, root):
        self.root = root
        self.style = ttk.Style()
        self.style.theme_use('clam')

        self.create_widgets()

    def create_widgets(self):
        self.function_label = ttk.Label(self.root, text="Select function:")
        self.function_label.grid(row=0, column=0, pady=10)
        self.function_var = tk.StringVar(self.root)
        self.function_var.set('Quadratic')  # default value
        self.function_option = tk.OptionMenu(self.root, self.function_var, 'Quadratic', 'Sine', 'Fractional', 'Exponential', 'Logarithmic', 'Composite')
        self.function_option.grid(row=0, column=1, pady=10)

        self.a_label, self.a_entry = self.create_entry("Enter a:", 1)
        self.b_label, self.b_entry = self.create_entry("Enter b:", 2)
        self.c_label, self.c_entry = self.create_entry("Enter c:", 3)

        self.plot_button = ttk.Button(self.root, text="Plot", command=self.plot_graph)
        self.plot_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.close_button = ttk.Button(self.root, text="Close", command=self.root.quit)
        self.close_button.grid(row=5, column=0, columnspan=2, pady=10)

    def create_entry(self, text, row):
        label = ttk.Label(self.root, text=text)
        label.grid(row=row, column=0, pady=10)
        entry = ttk.Entry(self.root)
        entry.grid(row=row, column=1, pady=10, padx=(0, 20))
        return label, entry

    def plot_graph(self):
        function_type = self.function_var.get()
        a = float(self.a_entry.get())
        b = float(self.b_entry.get())
        c = float(self.c_entry.get())

        x = np.linspace(-10, 10, 400)
        y, title = self.calculate_y_and_title(function_type, a, b, c, x)

        fig = plt.figure()
        plt.plot(x, y)
        plt.title(title)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True)

        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()
        canvas.get_tk_widget().grid(row=6, column=0, columnspan=4, pady=10)

    def calculate_y_and_title(self, function_type, a, b, c, x):
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
        return y, title

root = tk.Tk()
app = GUIApp(root)
root.mainloop()
