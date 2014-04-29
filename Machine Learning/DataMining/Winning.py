import matplotlib.pyplot as plt

__author__ = 'davidoregan'

import json
from operator import itemgetter
import pandas as pd
import thread
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import Imputer
from matplotlib import *


import warnings
warnings.filterwarnings('ignore')
pd.options.display.width = 900


training = pd.read_csv('wv_golf.csv')
print training.shape

training['mileage'] = training['mileage'].str.replace('M', '')
training['mileage'] = training['mileage'].str.replace(',', '')
training['price'] = training['price'].str.replace(',', '')
training['price'] = training['price'].str.replace('POA', '0')
training['mileage'] = training['mileage'].astype('float64')
training['price'] = training['price'].astype('float64')






training.fillna(0, inplace=True)
#training.values[:,:-1].astype(float)



print training.head(7)


training_no_price = training.drop(['price'], 1)
print training_no_price.head()



dv = DictVectorizer()
dv.fit(training.T.to_dict().values())


print dv.feature_names_

print training.dtypes

LR = LinearRegression().fit(dv.transform(training_no_price.T.to_dict().values()), training.price)
LR2 = ' + '.join([format(LR.intercept_, '0.2f')] + map(lambda (f,c): "(%0.2f %s)" % (c, f), zip(dv.feature_names_, LR.coef_)))

#print "Our model is such:        " + LR2

trainingErrs = abs(LR.predict(dv.transform(training.T.to_dict().values())) - training.price)


outlierIdx = trainingErrs
plt.scatter(training.mileage, training.price, c=(0,0,1), marker='s')
plt.scatter(training.mileage[outlierIdx], training.price[outlierIdx], c=(1,0,0), marker='s')

plt.show()
