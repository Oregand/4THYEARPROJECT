__author__ = 'davidoregan'

import pandas as pd
import numpy as np
import pylab as pl
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_extraction import DictVectorizer



df = pd.read_csv("wv_golfTraining.csv")

df['mileage'] = df['mileage'].str.replace('M', '')
df['mileage'] = df['mileage'].str.replace(',', '')
df['price'] = df['price'].str.replace(',', '')
df['price'] = df['price'].str.replace('POA', '0')
df['mileage'] = df['mileage'].astype('float64')
df['price'] = df['price'].astype('float64')


df.fillna(0, inplace=True)



test_idx = np.random.uniform(0, 1, len(df)) <= 0.3
train = df[test_idx==True]
test = df[test_idx==False]

features = ['mileage', 'carYear', 'Owners']

results = []
for n in range(1, 100, 2):
    clf = KNeighborsClassifier(n_neighbors=n)
    clf.fit(train[features], train['price'])
    preds = clf.predict(test[features])
    accuracy = np.where(preds==test['price'], 1, 0).sum() / float(len(test))
    print "Neighbors: %d, Accuracy: %3f" % (n, accuracy)

    results.append([n, accuracy])

results = pd.DataFrame(results, columns=["n", "accuracy"])

pl.plot(results.n, results.accuracy)
pl.title("Accuracy with Increasing K")
pl.show()
