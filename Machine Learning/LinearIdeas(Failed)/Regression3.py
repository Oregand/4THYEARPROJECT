__author__ = 'davidoregan'

from sklearn import linear_model
import matplotlib.pyplot as plt
import csv
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction import DictVectorizer



car_data = list(csv.DictReader(open('SVM', 'rU')))
car_target = open('MiscIdeas/../MiscIdeas/cartarget.csv', 'rU').read().splitlines()

vec = DictVectorizer()
car_data = vec.fit_transform(car_data).toarray()


# Use only one feature
houses_X = car_data[:, np.newaxis]
houses_X_temp = houses_X[:, :, 2]

X_train, X_test, y_train, y_test = train_test_split(houses_X_temp, car_target, test_size=0.33)

lreg = linear_model.LinearRegression()
lreg.fit(X_train, y_train)

plt.scatter(X_test, y_test, color='black')
plt.plot(X_test, lreg.predict(X_test), color='green', linewidth=3)

plt.show()