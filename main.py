

# Check for missing values
missing_values = df.isnull().sum()
print(missing_values)
df = df.dropna()  # or df['column_name'] = df['column_name'].fillna(df['column_name'].mean())

# Check for inconsistent entries
unique_values = df['column_name'].unique()
print(unique_values)
df['column_name'] = df['column_name'].str.lower()
df['column_name'] = df['column_name'].replace({'inconsistent_value1': 'correct_value', 'inconsistent_value2': 'correct_value'})

# Check for formatting errors
df['date_column'] = pd.to_datetime(df['date_column'], errors='coerce')
df['numeric_column'] = pd.to_numeric(df['numeric_column'], errors='coerce')

# Identify and handle outliers
Q1 = df['numeric_column'].quantile(0.25)
Q3 = df['numeric_column'].quantile(0.75)
IQR = Q3 - Q1
outliers = df[((df['numeric_column'] < (Q1 - 1.5 * IQR)) | (df['numeric_column'] > (Q3 + 1.5 * IQR)))]
print(outliers)
df = df[~((df['numeric_column'] < (Q1 - 1.5 * IQR)) | (df['numeric_column'] > (Q3 + 1.5 * IQR)))]
