# Graphing Calculator

This is a simple **Graphing Calculator** built using Python's **Tkinter** for the graphical user interface (GUI) and **Matplotlib** for plotting graphs. The calculator allows you to input mathematical equations, plot the graphs, and calculate `y` values for given `x` values, or solve for `x` given a `y` value.

## Features

- **Plotting Graphs**: You can enter an equation in the form `y = f(x)` (e.g., `sin(x)` or `x**2`) and plot its graph.
- **Find `y` for a given `x`**: Enter a value for `x` to find the corresponding `y` value.
- **Find `x` for a given `y`**: Enter a value for `y` to find the corresponding `x` value using numerical methods.
- **Help Menu**: A built-in help section provides instructions on how to use the calculator.
- **Support for Common Mathematical Functions**: The calculator supports functions like `sin`, `cos`, `tan`, `log`, `sqrt`, and constants like `pi` and `e`.

## Requirements

To run this project, you'll need to install the following libraries:

- **Tkinter**: For creating the GUI (usually comes pre-installed with Python).
- **Matplotlib**: For graphing and plotting.
- **NumPy**: For numerical calculations and handling mathematical operations.
- **SciPy**: For solving equations numerically to find `x` from `y`.

1. **Enter an Equation**: In the input field labeled "Enter Equation (y = f(x))", enter the mathematical expression for your graph. For example, you can enter `sin(x)`, `x**2`, or `tan(x)`.
2. **Plot the Graph**: Click the **Plot** button or press `Enter` to plot the graph of the equation.
3. **Find `y` for a given `x`**: Enter a value for `x` in the "Enter x Value" field and click **Find y** to get the corresponding `y` value.
4. **Find `x` for a given `y`**: Enter a value for `y` in the "Enter y Value" field and click **Find x** to get the corresponding `x` value.
5. **Help Menu**: Click on the **Help** menu at the top of the window and select **How to Use** to view instructions.




You can install the required dependencies using `pip`:

```bash
pip install matplotlib numpy scipy

