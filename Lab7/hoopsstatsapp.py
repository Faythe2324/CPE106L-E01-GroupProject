"""
File: hoopstatsapp.py

The application for analyzing basketball stats.
"""

# File: hoopstatsapp.py
# The application for analyzing basketball data.

import pandas as pd
from hoopstatsview import HoopStatsView

def cleanStats(df):
    """
    Cleans the basketball statistics DataFrame by splitting 'FG', '3PT', and 'FT' columns
    (formatted as 'makes-attempts') into separate numeric columns for makes and attempts.

    Parameters:
        df (DataFrame): The raw basketball statistics DataFrame.

    Returns:
        DataFrame: The cleaned DataFrame with separate columns for makes and attempts.
    """
    to_clean_items = {
        'FG': ('FGM', 'FGA'),
        '3PT': ('3PM', '3PA'),
        'FT': ('FTM', 'FTA')
    }

    df = df.copy()

    for col, (made_col, att_col) in to_clean_items.items():
        if col in df.columns:
            makes_attempts = df[col].astype(str).str.split('-', expand=True)
            df[made_col] = pd.to_numeric(makes_attempts[0], errors='coerce')
            df[att_col] = pd.to_numeric(makes_attempts[1], errors='coerce')
            df.drop(columns=[col], inplace=True)

    return df

def main():
    """Creates the data frame and view and starts the app."""
    frame = pd.read_csv('cleanbrogdonstats.csv')
    frame = cleanStats(frame)
    print(frame.head())  # Optional: preview cleaned data
    HoopStatsView(frame)

if __name__ == "__main__":
    main()


def cleanStats(df):
    """
    Cleans the basketball statistics DataFrame by splitting 'FG', '3PT', and 'FT' columns
    (formatted as 'makes-attempts') into separate numeric columns for makes and attempts.

    Parameters:
        df (DataFrame): The raw basketball statistics DataFrame.

    Returns:
        DataFrame: The cleaned DataFrame with separate columns for makes and attempts.
    """
    to_clean_items = {
        'FG': ('FGM', 'FGA'),
        '3PT': ('3PM', '3PA'),
        'FT': ('FTM', 'FTA')
    }

    df = df.copy()

    for col, (made_col, att_col) in to_clean_items.items():
        if col in df.columns:
            makes_attempts = df[col].astype(str).str.split('-', expand=True)
            df[made_col] = pd.to_numeric(makes_attempts[0], errors='coerce')
            df[att_col] = pd.to_numeric(makes_attempts[1], errors='coerce')
            df.drop(columns=[col], inplace=True)

    return df

def main():
    """Creates the data frame and view and starts the app."""
    frame = pd.read_csv('cleanbrogdonstats.csv')
    frame = cleanStats(frame)
    print(frame.head())  # Optional: preview cleaned data
    HoopStatsView(frame)

if __name__ == "__main__":
    main()
