import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

def analyze_bio_followers_correlation(users_csv_path='users.csv'):
    # Read the data
    df = pd.read_csv(users_csv_path)
    
    # Filter out rows without bios
    df = df[df['bio'].notna() & (df['bio'] != '')]
    
    # Calculate bio length in words (split by whitespace)
    df['bio_word_count'] = df['bio'].str.split().str.len()
    
    # Prepare data for regression
    X = df['bio_word_count'].values.reshape(-1, 1)
    y = df['followers'].values
    
    # Perform linear regression
    model = LinearRegression()
    model.fit(X, y)
    
    # Get the slope rounded to 3 decimal places
    slope = round(model.coef_[0], 3)
    
    # Print debug information
    print(f"Number of users with bios: {len(df)}")
    print(f"Bio word count range: {df['bio_word_count'].min()} to {df['bio_word_count'].max()}")
    print(f"Followers range: {df['followers'].min()} to {df['followers'].max()}")
    print(f"R-squared: {model.score(X, y):.3f}")
    
    return slope

# Calculate the regression slope
result = analyze_bio_followers_correlation()
print(f"\nRegression slope: {result:.3f}")
