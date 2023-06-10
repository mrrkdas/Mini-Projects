import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import (KNeighborsClassifier,
                               NeighborhoodComponentsAnalysis)
from sklearn.pipeline import Pipeline
import pandas as pd

#Jupyter NoteBook
df = pd.read_csv(r"file:///C:/Users/tube2/Downloads/car%20(1).data")

df.head()

df.rename(columns = {"vhigh": "buying", "vhigh.1": "maintenance price", "2": "doors", "2.1": "people", "small": "lug-boot", "low":"safety"}, inplace = True)

df.head()

#Label Encoding 
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df['buying_le'] = le.fit_transform(df['buying'])
df["maintenance price_le"] = le.fit_transform(df["maintenance price"])
df["doors_le"] = le.fit_transform(df["doors"])
df["people_le"] = le.fit_transform(df["people"])
df["lug-boot_le"] = le.fit_transform(df["lug-boot"])
df["safety_le"] = le.fit_transform(df["safety"])

df['buying'] = df['buying'].astype("category")
df["maintenance price"] = df["maintenance price"].astype("category")
df["doors"] = df["doors"].astype("category")
df["people"] = df["people"].astype("category")
df["lug-boot"] = df["lug-boot"].astype("category")
df["safety"] = df["safety"].astype("category")

df['buying'] = df['buying'].cat.codes
df["maintenance price"] = df["maintenance price"].cat.codes
df["doors"] = df["doors"].cat.codes
df["people"] = df["people"].cat.codes
df["lug-boot"] = df["lug-boot"].cat.codes
df["safety"] = df["safety"].cat.codes

df = df.drop(columns = ["buying_le", "maintenance price_le", "doors_le", "people_le", "lug-boot_le", "safety_le"])

X = df.drop("safety", axis = 1)
y = df["safety"]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2)



from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 5)
knn.fit(X_train, y_train)

knn.score(X_test, y_test) * 100

from sklearn.neighbors import RadiusNeighborsClassifier
rnc = RadiusNeighborsClassifier(algorithm = "kd_tree", weights = "uniform")
rnc.fit(X_train, y_train)

rnc.score(X_test, y_test) * 100

from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

classifiers = [Pipeline([('scaler', StandardScaler()),
                         ('knn', KNeighborsClassifier())
                         ]),
               Pipeline([('scaler', StandardScaler()),
                         ('rnc',  RadiusNeighborsClassifier())
                         ])]


names = ['knn',"scaler" 'rnc']
h = 0.01

x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))


for name, clf in zip(names, classifiers):

    clf.fit(X_train, y_train)
    score = clf.score(X_test, y_test)

    # Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, x_max]x[y_min, y_max].
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.figure()
    plt.pcolormesh(xx, yy, Z, cmap=cmap_light, alpha=.8)

    # Plot also the training and testing points
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold, edgecolor='k', s=20)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.title("{} (k = {})".format(name, n_neighbors))
    plt.text(0.9, 0.1, '{:.2f}'.format(score), size=15,
             ha='center', va='center', transform=plt.gca().transAxes)

plt.show()
