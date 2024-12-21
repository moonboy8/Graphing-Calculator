import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import tkinter.messagebox
from scipy.optimize import fsolve

def trigs(fom):
    # Replace common functions and constants with numpy equivalents
    fom = fom.replace("^", "**")  # Power operator (Python uses `**` for powers)
    fom = fom.replace("sin", "np.sin")  # Sine function
    fom = fom.replace("cos", "np.cos")  # Cosine function
    fom = fom.replace("tan", "np.tan")  # Tangent function
    fom = fom.replace("pi", "np.pi")  # Pi constant
    fom = fom.replace("e", "np.e")  # Euler's number constant
    fom = fom.replace("sqrt", "np.sqrt")  # Square root function
    fom = fom.replace("log", "np.log")  # Natural logarithm
    fom = fom.replace("ln", "np.log")  # Natural logarithm (alternative notation)
    fom = fom.replace("exp", "np.exp")  # Exponential function
    return fom

class GraphingCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Graphing Calculator")

        # Create a menu bar
        self.menu_bar = tk.Menu(master)
        master.config(menu=self.menu_bar)

        # Create Help menu
        self.help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(label="How to Use", command=self.show_help)

        # Create frame for main content and sidebar
        self.main_frame = tk.Frame(master)
        self.main_frame.pack(side=tk.LEFT, padx=20, pady=20)

        self.sidebar_frame = tk.Frame(master)
        self.sidebar_frame.pack(side=tk.RIGHT, padx=20, pady=20)

        # Create input field for equation with larger font
        self.equation_label = tk.Label(self.main_frame, text="Enter Equation (y = f(x)):", font=("Arial", 24))
        self.equation_label.pack(pady=10)
        self.equation_entry = tk.Entry(self.main_frame, font=("Arial", 20), width=20)
        self.equation_entry.pack(pady=10)

        # Create plot button with larger font
        self.plot_button = tk.Button(self.main_frame, text="Plot", command=self.plot_graph, font=("Arial", 20), height=3, width=12)
        self.plot_button.pack(pady=20)

        # Create figure and canvas for the plot with adjusted figure size
        self.fig = plt.figure(figsize=(12, 9))  # Even larger plot area
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.main_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()

        # Create the sidebar components
        self.x_value_label = tk.Label(self.sidebar_frame, text="Enter x Value:", font=("Arial", 18))
        self.x_value_label.pack(pady=10)
        self.x_value_entry = tk.Entry(self.sidebar_frame, font=("Arial", 16), width=10)
        self.x_value_entry.pack(pady=10)
        self.find_y_button = tk.Button(self.sidebar_frame, text="Find y", font=("Arial", 16), command=self.find_y_value, height=2, width=10)
        self.find_y_button.pack(pady=10)

        self.y_value_label = tk.Label(self.sidebar_frame, text="Enter y Value:", font=("Arial", 18))
        self.y_value_label.pack(pady=10)
        self.y_value_entry = tk.Entry(self.sidebar_frame, font=("Arial", 16), width=10)
        self.y_value_entry.pack(pady=10)
        self.find_x_button = tk.Button(self.sidebar_frame, text="Find x", font=("Arial", 16), command=self.find_x_value, height=2, width=10)
        self.find_x_button.pack(pady=10)

        # Bind the "Enter" key to the plot_graph method
        self.master.bind("<Return>", self.enter_pressed)

    def show_help(self):
        # Show a message box with instructions
        help_text = (
            "How to Use:\n\n"
            "1. Enter an equation in the form y = f(x) in the input field.\n"
            "   For example, enter 'sin(x)' or 'x**2'.\n\n"
            "2. Click 'Plot' or press Enter to plot the graph of the equation.\n\n"
            "3. To find the value of y for a specific x:\n"
            "   Enter a value for x in the 'Enter x Value' field and click 'Find y'.\n\n"
            "4. To find the value of x for a specific y:\n"
            "   Enter a value for y in the 'Enter y Value' field and click 'Find x'.\n\n"
            "Note: The equations can include common functions like sin, cos, tan, etc."
        )
        tk.messagebox.showinfo("Help", help_text)

    def plot_graph(self):
        try:
            equation = self.equation_entry.get()
            equation = trigs(equation)  # Preprocess the equation
            x = np.linspace(-10, 10, 1000)
            y = eval(equation)  # Evaluate the equation
            self.fig.clear()
            plt.plot(x, y)
            plt.grid(True)
            self.canvas.draw()

        except Exception as e:
            tk.messagebox.showerror("Error", f"Invalid equation: {e}")

    def find_y_value(self):
        try:
            equation = self.equation_entry.get()
            equation = trigs(equation)
            x_value = float(self.x_value_entry.get())
            # Evaluate the equation at the entered x-value
            y_value = eval(equation.replace("x", str(x_value)))
            # Display y value in a message box
            tk.messagebox.showinfo("Result", f"For x = {x_value}, y = {y_value}")
        except Exception as e:
            tk.messagebox.showerror("Error", f"Invalid input: {e}")

    def find_x_value(self):
        try:
            equation = self.equation_entry.get()
            equation = trigs(equation)
            y_value = float(self.y_value_entry.get())
            # Define the function to solve
            def equation_function(x):
                return eval(equation.replace("x", str(x))) - y_value
            # Use fsolve to find the corresponding x value for the given y
            x_solution = fsolve(equation_function, 0)[0]
            # Display x value in a message box
            tk.messagebox.showinfo("Result", f"For y = {y_value}, x = {x_solution}")
        except Exception as e:
            tk.messagebox.showerror("Error", f"Invalid input: {e}")

    def enter_pressed(self, event):
        self.plot_graph()  # Call plot_graph when "Enter" is pressed

root = tk.Tk()
calculator = GraphingCalculator(root)
root.mainloop()
