import numpy as np
import matplotlib.pyplot as plt

def plot_data(x, y, title='Data Plot', xlabel='X-axis', ylabel='Y-axis'):
    """
    Plots the given x and y data.

    Parameters:
    x (array-like): The x data points.
    y (array-like): The y data points.
    title (str): The title of the plot.
    xlabel (str): The label for the x-axis.
    ylabel (str): The label for the y-axis.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, marker='o', linestyle='-', color='b')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()
    print("Plot displayed successfully.")
    print(f"Data points: {len(x)}")
    print(f"X data: {x}")
    print(f"Y data: {y}")
    print("Plotting completed.")