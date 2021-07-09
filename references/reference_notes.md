# Summary of items worth revision

#### Artificial Intelligence
The effort to automate intellectual tasks normally performed by humans 

#### Classification 
In a classification problem, we are instead trying to predict results in a discrete output. In other words, we are trying to map input variables into discrete categories. 

#### Clustering  
Clustering: Take a collection of 1,000,000 different genes, and find a way to automatically group these genes into groups that are somehow similar or related by different variables, such as lifespan, location, roles, and so on.

#### DataFrame
A dataframe is datastructure in Pandas that holds the type of data you might think as a table. 

#### Features 
The columns that are inputted to our model and later used to make predictions are called *features*. Sometimes you will use all the columns except target as features. Othertimes you will be better off with fewer features.

#### Fitting / Training a model 
Capturing patterns from data is caled *fitting* or *training the model*. The data used to fit the model is called the *training data*

#### Kaggle - Getting started with a machine learning competition 
Initial steps to predict
- Understand the problem
- Exploratory Data Analysis (EDA)
- Train, tune & Ensemble ML models 
- Predict & receive accuracy score

Further steps to improve score 
- Learn more about data
- Experiment
    - Design / create some new features
    - Try different preprocessing 
    - Try different types of ML models
    - Combine multiple models (Ensemble)
- Learn from others code and ideas

#### Machine Learning 
A definition by Tom Mitchell, "A computer program is said to learn from experience E with respect to some class of tasks T and performance measure P, if it performance at tasks in T, as measured by P, improves with experience E."

#### MAE (mean_absolute_error)
To summarize the model quality in single metric through MAE. This value will say that predictions are off by that much value.  

#### max_leaf_nodes
max_leaf_nodes argument in skilearn DecisionTreeRegressor model provides a very sensible way to control overfitting and underfitting. 

#### Model Validation 
Model validation is to measure the quality of the model. Measuring model quality is the key to iteratively improving the model . One such way to do so to summarize model quality into a single metric MAE (mean_absolute_error)

#### Non-clustering
Non-clustering: The "Cocktail Party Algorithm", allows you to find structure in a chaotic environment. (i.e. identifying individual voices and music from a mesh of sounds at a cocktail party).

#### Overfitting
Where a model matches the training data almost perfectly, but does poorly in validation and other new data. 

#### Pandas
Pandas is the primary tool data scientist use for exploring and manipulating data 

#### RandomTreeRegressor  
The random forest uses many trees, and it makes a prediction by averaging the predictions of each component tree. It generally has much better predictive accuracy than a single decision tree and it works well with default parameters. If you keep modeling, you can learn more models with even better performance, but many of those are sensitive to getting the right parameters.  
scikit ref: `from sklearn.ensemble import RandomForestRegressor`

#### Regression
In a regression problem, we are trying to predict results within a continuous output, meaning that we are trying to map input variables to some continuous function.

#### Root-Mean-Squared-Error (RMSE)
Root Mean Square Error (RMSE) is the standard deviation of the residuals (prediction errors). Residuals are a measure of how far from the regression line data points are; RMSE is a measure of how spread out these residuals are.  
In other words, it tells you how concentrated the data is around the line of best fit. Root mean square error is commonly used in climatology, forecasting, and regression analysis to verify experimental results.

Ref: https://www.statisticshowto.com/probability-and-statistics/regression-analysis/rmse-root-mean-square-error/ 

#### Logarithm
In its simplest form, a logarithm answers the question: *How many of one number do we multiply to get another number?*  
We write "the number of 2s we need to multiply to get 8 is 3" as: log<sub>2</sub>(8) = 3

Notice we are dealing with three numbers:  
- The base: the number we are multiplying (a "2" in the example above)  
- How often to use it in a multiplication (3 times, which is the logarithm)  
- The number we want to get (an "8")  

#### scikit-learn
scikit-learn is easily the most popular library for modelling the types of data typically stored in DataFrames.

#### Steps in building and using a model
- Define - the type of model to be used 
- Fit - capture patterns from provided data. This is the *heart* of modelling
- Predict
- Evaluate - determine the accuracy of model's prediction

#### Supervised learning
In supervised learning, we are given a data set and already know what our correct output should look like, having the idea that there is a relationship between the input and the output.
Supervised learning problems are categorized into "regression" and "classification" problems. 

#### Underfitting
When a model fails to capture important distinctions and patterns in the data, so it performs poorly even in training data that is called underfitting. 

#### Unsupervised learning 
Unsupervised learning allows us to approach problems with little or no idea what our results should look like. We can derive structure from data where we don't necessarily know the effect of the variables.
We can derive this structure by clustering the data based on relationships among the variables in the data.  
With unsupervised learning there is no feedback based on the prediction results.

#### Validation Data
Model's practical value comes from making predictions on new data. we measure performance on data that wasn't used to build the model. The most straightforward way to do this is to exclude some data from model building process and then use these to test the model's accuracy on data it hasn't seen before. This data is called validation data