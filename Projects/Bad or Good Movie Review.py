
import pandas as pd
import numpy as np
import sklearn

df = pd.read_csv("moviereviews2.tsv", sep = "\t")
df.dropna(inplace = True)

from sklearn.model_selection import train_test_split

X = df["review"]
y = df["label"]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3)

from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline

text_clf1 = Pipeline([('tfidf', TfidfVectorizer()),
                     ('clf', LinearSVC())])

text_clf1.fit(X_train, y_train)

input_ = input("Review: ")

pred = text_clf1.predict([input_])

if pred == 'pos':
    print('Positive Review')
else:
    print('Negative Review')





