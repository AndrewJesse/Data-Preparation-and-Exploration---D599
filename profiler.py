import pandas as pd

def profiler(df, column_name, ascending=True):
    # Define a variable that holds the array of unique values of column_name
    unique_values = df[column_name].unique()  # Get unique values including NaN

    # Convert NaN to None for display purposes
    unique_values = [None if pd.isna(x) else x for x in unique_values]

    # Sort the unique values, treating None as the largest or smallest based on order
    unique_values = sorted(unique_values, key=lambda x: (x is None, x), reverse=not ascending)

    # Strip column_name from df and make it into a new DataFrame
    column_df = df[[column_name]]

    # Print the unique values of column_name
    print(f"Unique values in '{column_name}' (sorted):")
    print(unique_values)

    # Print the describe() output of the column_name DataFrame
    print(f"\nDescribe output for '{column_name}':")
    print(column_df.describe())

    return column_df
