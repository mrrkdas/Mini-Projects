#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd

df = pd.read_csv('smsspamcollection.tsv', sep = '\t')
df.head()


from sklearn.model_selection import train_test_split

X = df["message"]
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33)


from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier

clf_3 = Pipeline([('tfidf', TfidfVectorizer()),
                 ('clf', SGDClassifier())])

clf_3.fit(X_train, y_train)


message = input('Input your message: ')

prediction = clf_3.predict([message])


if prediction == 'ham':
    print('\nThis is a real message, not a spam')
else:
    print('\nThis is a spam message, DO NOT reply, and block the number/email immediately')


# In[ ]:



