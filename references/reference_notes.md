# Summary of items worth revision

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

#### MAE (mean_absolute_error)
To summarize the model quality in single metric through MAE. This value will say that predictions are off by that much value.  

#### Model Validation 
Model validation is to measure the quality of the model. Measuring model quality is the key to iteratively improving the model . One such way to do so to summarize model quality into a single metric MAE (mean_absolute_error)

#### Pandas
Pandas is the primary tool data scientist use for exploring and manipulating data 

#### scikit-learn
scikit-learn is easily the most popular library for modelling the types of data typically stored in DataFrames.

#### Steps in building and using a model
- Define - the type of model to be used 
- Fit - capture patterns from provided data. This is the *heart* of modelling
- Predict
- Evaluate - determine the accuracy of model's prediction

#### Validation Data
Model's practical value comes from making predictions on new data. we measure performance on data that wasn't used to build the model. The most straightforward way to do this is to exclude some data from model building process and then use these to test the model's accuracy on data it hasn't seen before. This data is called validation data