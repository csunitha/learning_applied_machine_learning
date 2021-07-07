# A repository to capture Applied ML learning journey 
## Daily Progress 

### Day 5
**Coursera - Week1**  
Definition of ML, types of ML - supervised and unsupervised.   
Supervised learning - right answer.  
Regression - predict continuous value output.  
Classification - Discrete value output.  

**Kaggle - Intro to ML - Lesson4**
- underfitting and overfitting 
- finding the optimum 'max_leaf_nodes' to be set for DecisionTreeRegressor model using mae

### Day 4
**Kaggle - Intro to ML - Lesson4**
- Model Validation
- Train Test Split
- MAE (Mean_Absolute_Error)
Exercise using sklearn.metrics mean_absolute_error, sklearn.model_selection train_test_split

### Day 3
**TensorFlow - Machine Learning Foundations - ep 1.**
- Keras Framework - Layers, Neurons, dense 
- Installed tensorflow 
- The core of how a network learns is in these 2 parameters - optimizer and loss. 
Thanks to this diagram in Francois Chollet's book Deep Learning with Python - i could clearly understand.
Image link: [![deeplearning-simpleformat](/references/deeplearning-simpleformat.jpg "Deep learning in simple format")]
Exercise - Tried predict house prices using keras sequential, optimizer sgd and loss mean_squared_error 

**Kaggle - Intro to ML - Lesson3**  
Got introduced to scikit-learn, DecisionTreeRegressor model. 
Exercise - Using sklearn tree - DecisionTreeRegressor to predict Iowa home sale price. 
Followed these steps to define, fit, predict and evaluate. 

### Day 2
Started the Intro to ML course in Kaggle. (https://www.kaggle.com/learn/intro-to-machine-learning)
Learnt the following through analyzing Melbourne and Iowa housing data. Lessons 1-3
- Opening a csv file and loading into data frame -> pd.read_csv(filepath)
- List out the columns -> df.columns
- Describe and get the values - count, mean, std, min, 25%, 50%, 75%, max -> df.describe(). df[['col1','col3']].describe()

Also learnt to select prediction target(y) and features(X) that would be used for prediction 
example 
y = df.colname
X = df['col1', 'col2', 'col5']

Also read about standard deviation (population and sample), σ from awesome link https://www.mathsisfun.com/data/standard-deviation.html

Also trying my hand with getting a fair understanding of git branching and commit. 

### Day 1
Finished the python course in Kaggle and tried first exercise of titanic survival prediction in kaggle tutorial. Along with that, did the same code in my local vscode.
Day1 is 3-Jul-2021.
