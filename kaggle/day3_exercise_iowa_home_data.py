import pandas as pd

filepath = "kaggle/input/iowa_home_data/train.csv"
home_data = pd.read_csv(filepath)

# describe for all columns
print(home_data.describe())

# list all columns 
print(home_data.columns)

# specify prediction target 
y = home_data.SalePrice

# define predictive features 
feature_names = ['LotArea',  'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
X = home_data[feature_names]

# define model 
from sklearn.tree import DecisionTreeRegressor
iowa_model = DecisionTreeRegressor(random_state=1)

# fit model
iowa_model.fit(X, y)

# predictions for X
predictions = iowa_model.predict(X)

print(predictions)

print(home_data['SalePrice'].head())