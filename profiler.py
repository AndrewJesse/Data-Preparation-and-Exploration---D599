def profiler(df, column_name):
    # Define a variable that holds the array of unique values of column_name
    unique_values = df[column_name].unique()

    # Strip column_name from df and make it into a new DataFrame
    column_df = df[[column_name]]

    # Print the unique values of column_name
    print(f"Unique values in '{column_name}':")
    print(unique_values)

    # Print the describe() output of the column_name DataFrame
    print(f"\nDescribe output for '{column_name}':")
    print(column_df.describe())

    return column_df

