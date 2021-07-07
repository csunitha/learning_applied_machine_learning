import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

# read the data and cleanup
filepath = 'kaggle/input/iowa_home_data/train.csv'
iowa_home_data = pd.read_csv(filepath)

# set target and prediction 
y = iowa_home_data.SalePrice
predictionFeatures =  ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
X = iowa_home_data[predictionFeatures]

# split into train and validation data 
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 1)

# specify the model and fit 
model = DecisionTreeRegressor(random_state=1)
model.fit(train_X, train_y)

# calculate MAE (mean_absolute_error)
val_predictions =  model.predict(val_X)
val_mae = mean_absolute_error(val_y, val_predictions)

# define a new function to get mae
def get_mae(max_leaf_nodes, train_X, test_X, train_y, test_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state = 0)
    model.fit(train_X, train_y)
    predicted_value = model.predict(test_X)
    mae = mean_absolute_error(test_y, predicted_value)
    return mae

candidate_max_leaf_nodes = [5, 25, 50, 100, 250, 500]
min_mae = None
optimum_leaf_node = None
for leaf_node_value in candidate_max_leaf_nodes:
    mae = get_mae(leaf_node_value, train_X, val_X, train_y, val_y)
    print("Validation MAE: {:,.0f} for leaf node: {}".format(mae, leaf_node_value))
    if(min_mae == None):
        min_mae = mae
        optimum_leaf_node = leaf_node_value
    elif(mae < min_mae):
        min_mae = mae 
        optimum_leaf_node = leaf_node_value

# Store the best value of max_leaf_nodes (it will be either 5, 25, 50, 100, 250 or 500)
print("\n\nOptimum MAE: {:,.0f} is in leaf node: {}".format(min_mae, optimum_leaf_node))

#################  alternate efficient way of doing the above loop using dictionary ################
scores = {leaf_size: get_mae(leaf_size, train_X, val_X, train_y, val_y) for leaf_size in candidate_max_leaf_nodes}
best_tree_size = min(scores, key=scores.get)
print("\n\nBest tree size is : {}".format(best_tree_size))

## now create model with the best fit and predict
final_model = DecisionTreeRegressor(max_leaf_nodes = best_tree_size, random_state=1)

# fit the final model 
final_model.fit(X, y)



