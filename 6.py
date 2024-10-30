import csv
from collections import Counter
from datetime import datetime

# Step 1: Get logins of users who joined after 2020
users_after_2020 = set()

# Read the users.csv file to find users who joined after 2020
with open('users.csv', 'r', encoding='utf-8') as users_file:
    users_reader = csv.DictReader(users_file)
    for row in users_reader:
        created_at = row.get('created_at', '').strip()
        
        if created_at:
            user_join_date = datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%SZ")
            if user_join_date.year > 2020:
                users_after_2020.add(row['login'])

# Step 2: Collect programming languages from repositories of these users
languages = []

# Read the repositories.csv file to get languages for users who joined after 2020
with open('repositories.csv', 'r', encoding='utf-8') as repos_file:
    repos_reader = csv.DictReader(repos_file)
    for row in repos_reader:
        if row['login'] in users_after_2020:
            language = row.get('language', '').strip()
            if language:
                languages.append(language)

# Count the occurrence of each language
language_counts = Counter(languages)

# Get the two most common languages
most_common_languages = language_counts.most_common(2)

# Print the second most common language
if len(most_common_languages) >= 2:
    print(most_common_languages[1][0])  # Second most common language
else:
    print("Not enough language data found.")
