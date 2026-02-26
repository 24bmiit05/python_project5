import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


def draw_plot():
    # 1️⃣ Import data
    df = pd.read_csv("epa-sea-level.csv")

    # 2️⃣ Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # 3️⃣ Line of best fit (1880–latest year)
    res = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Create years through 2050
    years_extended = np.arange(df["Year"].min(), 2051)
    sea_level_predicted = res.intercept + res.slope * years_extended

    ax.plot(years_extended, sea_level_predicted, color="red")

    # 4️⃣ Line of best fit (2000–latest year)
    df_2000 = df[df["Year"] >= 2000]

    res_2000 = linregress(df_2000["Year"], df_2000["CSIRO Adjusted Sea Level"])

    years_extended_2000 = np.arange(2000, 2051)
    sea_level_predicted_2000 = (
        res_2000.intercept + res_2000.slope * years_extended_2000
    )

    ax.plot(years_extended_2000, sea_level_predicted_2000, color="green")

    # 5️⃣ Labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")

    fig.savefig("sea_level_plot.png")
    return fig