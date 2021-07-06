import pandas as pd

# read the data and cleanup
filepath = 'kaggle/input/iowa_home_data/train.csv'
iowa_home_data = pd.read_csv(filepath)

# print(" ******* home data **********")
# print(iowa_home_data.columns)
# print(iowa_home_data.head())

# set target and prediction 
y = iowa_home_data.SalePrice
predictionFeatures =  ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
X = iowa_home_data[predictionFeatures]

# define model
from sklearn.tree import DecisionTreeRegressor
model = DecisionTreeRegressor()
model.fit(X,y)

#  In-sample predictions vs Actual Price
print("\n\n******** In-Sample Predictions ********")
print("In-Sample predictions", model.predict(X.head()))
print("Actual Sale Price    ", y.head().tolist())

# train and test data split 
from sklearn.model_selection import train_test_split
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 1)

model = DecisionTreeRegressor(random_state=1)
model.fit(train_X, train_y)

#  train and test predictions vs Actual Price
print("\n\n ******** Train and Test split Predictions ********")
print("Test predicted Price    ", model.predict(val_X.head()))
print("Test actual Sale Price  ", val_y.head().tolist())

# calculate MAE (mean_absolute_error)
from sklearn.metrics import mean_absolute_error
val_predictions =  model.predict(val_X)

print("\n\n MAE with train and split data", mean_absolute_error(val_y, val_predictions), "\n\n")