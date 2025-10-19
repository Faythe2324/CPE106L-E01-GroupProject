# Program to load, clean, and plot average bread prices by year

import pandas as pd
import matplotlib.pyplot as plt

def load_and_clean(filepath):
    # Skip the first 10 rows of metadata before the header row
    df = pd.read_csv(filepath, skiprows=10)
    df.replace("", pd.NA, inplace=True)
    # Rename the first column to "Year"
    df.rename(columns={df.columns[0]: "Year"}, inplace=True)
    # Identify month columns (Jan–Dec)
    month_columns = df.columns[1:]
    df[month_columns] = df[month_columns].apply(pd.to_numeric, errors="coerce")
    # Compute the average bread price per year
    df["AvgPrice"] = df[month_columns].mean(axis=1)

    # Return only the Year and AvgPrice columns
    return df[["Year", "AvgPrice"]]

def plot_prices(df):
    plt.figure(figsize=(10, 6))
    plt.plot(df["Year"], df["AvgPrice"], marker="o", linestyle="-", color="b")
    plt.title("Average Bread Price by Year")
    plt.xlabel("Year")
    plt.ylabel("Average Price (USD)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def main():
    filepath = "breadprice.csv"  # make sure it's in the same folder
    df = load_and_clean(filepath)
    print(df)
    plot_prices(df)

if __name__ == "__main__":
    main()
