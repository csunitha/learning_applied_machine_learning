import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

import os

for dirname, _, filenames in os.walk('kaggle/input/day1_titanic'):
    for filename in filenames:
        print(os.path.join(dirname, filename))


#loading the training data
train_data = pd.read_csv("kaggle/input/day1_titanic/train.csv")
print(train_data.head())

#loading the test data 
test_data = pd.read_csv("kaggle/input/day1_titanic/test.csv")
print(test_data.head())

#exploring a pattern
women = train_data.loc[train_data.Sex == 'female']['Survived']
rate_women = sum(women)/len(women)

print("% of women who survived: ", rate_women)

men = train_data.loc[train_data.Sex == 'male']['Survived']
rate_men = sum(men)/len(men)

print("% of men who survived: ", rate_men)

#first machine learning model using Random Forest Model 
from sklearn.ensemble import RandomForestClassifier

y = train_data['Survived']

features = ["Pclass", "Sex", "SibSp", "Parch"]
X = pd.get_dummies(train_data[features])
X_test = pd.get_dummies(test_data[features])

model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)
model.fit(X, y)
predictions = model.predict(X_test)

output = pd.DataFrame({'PassengerId' : test_data.PassengerId, 'Survived' : predictions})
output.to_csv("kaggle/output/day1_my_submission1.csv", index=False)

print("Your submission was successfully saved!")