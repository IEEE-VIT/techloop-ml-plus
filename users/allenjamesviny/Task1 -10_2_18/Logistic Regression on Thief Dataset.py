
# coding: utf-8

# In[13]:


import pandas as pd
#import pandas.DataFrame as df
import numpy as np
from sklearn.metrics import precision_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
get_ipython().run_line_magic('matplotlib', 'inline')

thief = pd.read_csv("C:\Criminal\criminal_train_2.csv") #load .csv file to train the model
thief_test=pd.read_csv("C:\Criminal\criminal_test.csv")#load .csv file to test the model

y = thief['Criminal']
X = thief.drop('Criminal', axis = 1)

#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

sc = StandardScaler()
X = sc.fit_transform(X)
thief_test = sc.fit_transform(thief_test)

rfc = LogisticRegression(C=0.001)
rfc.fit(X, y)
pred_rfc = rfc.predict(thief_test)

y_new=pd.DataFrame(y)
y_new = y_new[:11430]

print(classification_report(y_new, pred_rfc))

print(confusion_matrix(y_new, pred_rfc))# to determine the accuracy of the model

precision_score(y_new,pred_rfc,average=None)

