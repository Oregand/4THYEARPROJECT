__author__ = 'davidoregan'

import csv
from sklearn.feature_extraction import DictVectorizer
from sklearn import preprocessing
from sklearn.cross_validation import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import cross_validation
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


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


""" After prepping the data and labels by encoding them, it's time to split up the dataset using train_test_split(), to avoid overfitting later on.

"""

car_data_train, car_data_test, target_train, target_test = train_test_split(car_data, target)


""" It's now time to build our classifier! Using the Naive Bayes classifier is easy (if you want to learn more about it, check out the supervised learning notebook).

"""

nb_estimator = GaussianNB()
nb_estimator.fit(car_data_train, target_train)
pred = nb_estimator.predict(car_data_test)


""" Simple LR """



#print car_data[10]

print 'Data instance:', car_data[10]
print 'Label:', car_target[10]

print 'Vectorized:', car_data[10]
print 'Unvectorized:', vec.inverse_transform(car_data[10])

print 'Transformed:', target[10]
print 'Inverse transformed:', le.inverse_transform(target[10])

print 'Training set:', len(car_data_train)
print 'Test set:', len(car_data_test)

print 'Predicted labels:', pred[0:8]
print 'Actual labels:', target_test[0:8]

print 'Predicted labels inverse:', list(le.inverse_transform(pred[0:8]))
print 'Actual labels inverse:', list(le.inverse_transform(target_test[0:8]))


print 'Score:', nb_estimator.score(car_data_test, target_test)

print 'Cross validation scoring:', cross_validation.cross_val_score(nb_estimator,
                                                                    car_data_test,
                                                                    target_test, cv=4)



