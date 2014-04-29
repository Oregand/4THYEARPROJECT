__author__ = 'davidoregan'

import pandas as pd
from sklearn.ensemble import ExtraTreesClassifier
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split
from sklearn import svm

#trying to make a all rows of the first column and b all rows of columns 2-46, i.e., a will be only target data (rent prices) and b will be the data.


rentdata = pd.read_csv('output.csv')
yolo = rentdata.head()
a, b = rentdata.head(0), rentdata.iloc[1:7]

X = rentdata[: 7]
y = rentdata[: 5]

clf = svm.SVC()
clf.fit(X, y)

clf.predict([[2., 2.]])