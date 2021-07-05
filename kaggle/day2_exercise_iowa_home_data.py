import pandas as pd

filepath = "kaggle/input/day2_exercise_iowa_home_data/train.csv"
home_data = pd.read_csv(filepath)

# describe for all columns
print(home_data.describe())

# list all columns 
print(home_data.columns)

# describe for specific columns
print(home_data[['YrSold','YearBuilt']].describe())

#questions and answers 
# What is the average lot size (rounded to nearest integer)?
# avg_lot_size = 10517

# As of today, how old is the newest home (current year - the date in which it was built)
# newest_home_age = 11