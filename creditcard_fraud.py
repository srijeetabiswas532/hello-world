#!/usr/bin/env python
# coding: utf-8

# In[8]:



# importing needed packages
import numpy as np
import pandas as pd
import matplotlib as mpl
import seaborn
import scipy
import sklearn
import matplotlib.pyplot as plt

# reading in file
data = pd.read_csv('creditcard.csv')
print(data.columns)


# In[7]:


# exploring file
print(data.describe())


# In[10]:


data = data.sample(frac = 0.1, random_state = 1)
print(data.shape)


# In[15]:


import matplotlib.pyplot as plt
data.hist(figsize = (20,20))
plt.show()


# In[16]:


# assigning numerical 'tells'
Fraud = data[data['Class'] == 1]
Valid = data[data['Class'] == 0]

outlier_frac = len(Fraud)/float(len(Valid))
print(outlier_frac)
print(len(Fraud))
print(len(Valid))


# In[18]:


correlation_mat = data.corr()
figure = plt.figure(figsize = (12,9))
seaborn.heatmap(correlation_mat, vmax = .8, square = True)
plt.show()


# In[19]:


# getting rid of class column
cols = data.columns.tolist()
cols = [c for c in cols if c not in ["Class"]]
target = "Class"

# supervised learning
x = data[cols]
y = data[target]

print(x.shape)
print(y.shape)


# In[23]:


from sklearn.metrics import classification_report, accuracy_score
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor

state = 1

# dictionary of classifiers
classifiers = { 
    "Isolation Forest": IsolationForest(max_samples=len(x),
                                       contamination = outlier_frac,
                                       random_state = state),
    "Local Outlier Factor": LocalOutlierFactor(
    n_neighbors = 20,
    contamination = outlier_frac)
}

n_outliers = len(Fraud)

for i, (clf_name, clf) in enumerate(classifiers.items()):
    
    if clf_name == "Local Outlier Factor":
        y_pred = clf.fit_predict(x)
        scores_pred = clf.negative_outlier_factor_
    else:
        clf.fit(x)
        scores_pred = clf.decision_function(x)
        y_pred = clf.predict(x)
        
    y_pred[y_pred == 1] = 0
    y_pred[y_pred == -1] = 1
    
    n_errors = (y_pred != y).sum()
    
    print('{}: {}'.format(clf_name,n_errors))
    print(accuracy_score(y,y_pred))
    print(classification_report(y,y_pred))


# In[ ]:




