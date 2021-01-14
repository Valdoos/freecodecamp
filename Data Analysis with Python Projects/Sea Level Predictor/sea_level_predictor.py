import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    file = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(file["Year"],file["CSIRO Adjusted Sea Level"],4)

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(file["Year"],file["CSIRO Adjusted Sea Level"])
    predict = pd.DataFrame([[x,slope*x+intercept] for x in range(1880,2050)],columns = ["Year","CSIRO Adjusted Sea Level"])
    plt.plot(predict["Year"],predict["CSIRO Adjusted Sea Level"])
    # Create second line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(file[file["Year"]>=2000]["Year"],file[file["Year"]>=2000]["CSIRO Adjusted Sea Level"])
    predict = pd.DataFrame([[x,slope*x+intercept] for x in range(2000,2050)],columns = ["Year","CSIRO Adjusted Sea Level"])
    plt.plot(predict["Year"],predict["CSIRO Adjusted Sea Level"])

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
