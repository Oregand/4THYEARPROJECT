__author__ = 'davidoregan'

import csv
from sklearn.feature_extraction import DictVectorizer
from sklearn import preprocessing
from sklearn.cross_validation import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import linear_model
import matplotlib.pyplot as plt
import numpy as np

""" Read in data from CSV's """

car_data = list(csv.DictReader(open('SVM', 'rU')))
car_target = open('MiscIdeas/../MiscIdeas/cartarget.csv', 'rU').read().splitlines()

""" Next is to vectorize and encode my categorical variables, as discessed in the data preprocessing notebook. """
vec = DictVectorizer()
car_data = vec.fit_transform(car_data).toarray()

""" I also have to encode the labels, since they're currently in text form. You can get the original label using the inverse_transform() function.

 """

le = preprocessing.LabelEncoder()
le.fit(["goodDeal", "badDeal"])
#le.fit(["unacc", "acc", "good", "vgood"])
target = le.transform(car_target)


train_X, test_X, train_y, test_y = train_test_split(car_data, target, test_size=0.33)

nb_estimator = GaussianNB()
nb_estimator.fit(train_X, train_y)
pred = nb_estimator.predict(test_X)


print 'Predicted labels:', pred[0:8]
print 'Actual labels:', test_y[0:8]




car_data2 = car_data[:, np.newaxis]
car_dataTemp = car_data2[:, :, 2]


X_train, X_test, y_train, y_test = train_test_split(car_dataTemp, target, test_size=0.33)

lreg = linear_model.LinearRegression()
lreg.fit(X_train, y_train)

plt.scatter(X_test, y_test, color='black')
plt.plot(X_test, lreg.predict(X_test), color='green', linewidth=3)

print X_test
print lreg.predict(X_test)

plt.show()
