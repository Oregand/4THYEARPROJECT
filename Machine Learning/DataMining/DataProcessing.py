__author__ = 'davidoregan'

import csv
from sklearn.feature_extraction import DictVectorizer
from sklearn import preprocessing
from sklearn.cross_validation import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import cross_validation
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

from sklearn import linear_model


""" Read in data from CSV's """

car_data = list(csv.DictReader(open('../SVM', 'rU')))
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

""" Linear Regssion Time brah """

lreg = linear_model.LinearRegression()
lin = lreg.fit(car_data_train, target_train)



'''
print lin
print b_0
print coeff
'''



pca = PCA(n_components=2)
X_test_r = pca.fit(car_data_test).transform(car_data_test)

kmeans = KMeans(n_clusters=10)
kmeans.fit(X_test_r)
centroids = kmeans.cluster_centers_
target_names = le.classes_

plt.figure()
for c, i, target_name in zip(['b', 'r', 'g', 'c'],
                             [0, 1, 2, 3], target_names):
    plt.plot(X_test_r[target_test == i, 0], X_test_r[target_test == i, 1], 'o',
             c=c, markeredgecolor='k', markersize=8, label=target_name)
    plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', s=300, linewidths=5,
                color='chartreuse', zorder=10)

plt.legend()
plt.show()



#4plt.scatter(car_data_test, target_test, color='black')
#plt.plot(car_data_test, lreg.predict(car_data_test), color='green', linewidth=3)
#plt.show()





