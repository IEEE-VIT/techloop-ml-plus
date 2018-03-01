import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Data.csv', index=False)
X = dataset.iloc[:, 0:3].values
y = dataset.iloc[:, 3].values



#Handling Missing Values
from sklearn.preprocessing import Imputer
age_and_salary = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
X[:, 1:3] = age_and_salary.fit_transform(X[:, 1:3])



#Handling Categorical values
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])
onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray()

labelencoder_y = LabelEncoder()
y[:,0] = labelencoder_y.fit_transform(y[:,0])

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)