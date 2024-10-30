import pandas as pd

# Load the CSV file
csv_file = 'repositories.csv'  # Replace with the correct path

# Load the CSV into a DataFrame
df = pd.read_csv(csv_file)

# Convert 'has_projects' and 'has_wiki' to integer (0 or 1) for correlation calculation
df['has_projects'] = df['has_projects'].astype(int)
df['has_wiki'] = df['has_wiki'].astype(int)

# Calculate the Pearson correlation
correlation = df['has_projects'].corr(df['has_wiki'])

# Print the correlation rounded to 3 decimal places
print(f"Correlation between projects and wiki enabled: {correlation:.3f}")
