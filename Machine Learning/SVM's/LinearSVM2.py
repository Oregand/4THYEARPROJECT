__author__ = 'davidoregan'

from sklearn.feature_extraction.text import CountVectorizer


import pandas as pd
import numpy as np

train_data = pd.read_csv("output.csv")
test_data = pd.read_csv("output.csv")

y_train = np.array(train_data.title)
comments_train = np.array(train_data.price)
print(comments_train.shape)
print(y_train.shape)


print(comments_train[0])
print("title: ", y_train[0])

print(comments_train[5])
print("title:", y_train[5])


cv = CountVectorizer()
cv.fit(comments_train)
print(cv.get_feature_names()[:15])

print " "

print(cv.get_feature_names()[1:10])

print " "

X_train = cv.transform(comments_train).tocsr()
print("X_train.shape: %s" % str(X_train.shape))
print(X_train[0, :])


print " "


from sklearn.svm import LinearSVC
svm = LinearSVC()
svm.fit(X_train, y_train)

comments_test = np.array(test_data.price)

y_test = np.array(test_data.title).astype(str)
X_test = cv.transform(comments_test).astype(str)

svm.score(X_test, y_test)