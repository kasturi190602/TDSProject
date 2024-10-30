# GitHub Users in Seattle

This repository contains data about GitHub users located in Seattle with over 200 followers, as well as information about their public repositories.

1. How I Gathered the Data: I used the GitHub API to pull details on users in Seattle with more than 200 followers, then grabbed info on their public repositories and organized it all into CSV files.

2. A Surprising Find: One interesting thing I noticed was that a lot of high-follower users in Seattle aren’t all tied to big tech companies; quite a few are actually working solo or as freelancers.

3. Advice for Other Developers: If you're looking to build a following, keeping your GitHub profile and projects updated seems to make a difference – people are definitely paying attention to activity and recent work.

## Files

1. `users.csv`: Contains details of GitHub users in Seattle with more than 200 followers.
2. `repositories.csv`: Contains data on up to 500 public repositories for each user listed in `users.csv`.
3. `gitscrap.py`: Python script used to collect and format this data.

## Data Collection

- Data was collected using the GitHub API on 2024-10-30.
- The dataset includes users based in Seattle with a minimum of 200 followers.
- For each user, up to 500 of their most recently pushed repositories are included.

