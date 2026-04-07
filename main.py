from pyscript import display, document
import numpy as np
import matplotlib.pyplot as plt

def sample_numpy(e):
    # Clear the previous text content in the output div
    document.getElementById('output').innerHTML = ""

    # Setting up the data
    days = np.array(['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun'])
    sold_bags = np.array([4, 2, 3, 4, 7, 3, 1])
    
    # Create the plot
    plt.figure(figsize=(8, 4)) # Sets the size of the graph
    plt.plot(days, sold_bags, marker='o')

    # --- Adding your labels here ---
    plt.title("Donuts Sold")  # adding the graph title
    plt.xlabel("Days")        # adding the x label
    plt.ylabel("Bags Sold")   # adding the y label (changed to bags to match!)

    # Display the result in the HTML
    display(plt, target="output")