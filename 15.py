import pandas as pd

def analyze_email_sharing(users_csv_path='users.csv'):
    # Read the complete CSV file
    df = pd.read_csv(users_csv_path)
    
    # Convert email column to boolean (True if email exists, False if NaN or empty)
    df['has_email'] = df['email'].notna() & (df['email'] != '')
    
    # Calculate for hireable users
    hireable_email_fraction = df[df['hireable'] == True]['has_email'].mean()
    
    # Calculate for non-hireable users
    non_hireable_email_fraction = df[df['hireable'] != True]['has_email'].mean()
    
    # Calculate difference and round to 3 decimal places
    difference = round(hireable_email_fraction - non_hireable_email_fraction, 3)
    
    # Print debug information
    print(f"Total users: {len(df)}")
    print(f"Hireable users with email: {df[df['hireable'] == True]['has_email'].sum()}/{(df['hireable'] == True).sum()}")
    print(f"Non-hireable users with email: {df[df['hireable'] != True]['has_email'].sum()}/{(df['hireable'] != True).sum()}")
    print(f"Hireable fraction: {hireable_email_fraction:.3f}")
    print(f"Non-hireable fraction: {non_hireable_email_fraction:.3f}")
    
    return difference

# Read and analyze the complete dataset
result = analyze_email_sharing()
print(f"\nFinal result: {result:.3f}")
