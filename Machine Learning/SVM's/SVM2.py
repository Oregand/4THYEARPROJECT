__author__ = 'davidoregan'

import numpy as np
from sklearn import svm
import pandas as pd
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_extraction import DictVectorizer
import numpy as np


from ast import literal_eval


vec = DictVectorizer()
mydata2 = pd.read_csv('output.csv')
with open("SVM's/output.csv") as f:
       dic = literal_eval('{' + f.read() +'}')
       print dic


#pos_vectorized = vec.fit_transform(mydata2)



















#mydata = np.genfromtext('output.csv', delimiter=",")
#data_train = np.loadtxt('output.csv', delimiter=',',skiprows=1, usecols=(3, 4, ))
#as X = data_train[:, 1:]
#as y = data_train[:, 0].astype(np.int)
#as clf = ExtraTreesClassifier(n_estimators=100).fit(X, y)
#target = mydata2["title"]  #provided your csv has header row, and the label column is named "Label"
#select all but the last column as data
#data = mydata2.ix[:,:-1]
#print data['mileage']
#print mydata2






