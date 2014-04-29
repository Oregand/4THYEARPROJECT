__author__ = 'davidoregan'

import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from scipy import stats



from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import ast
from sklearn import preprocessing

data = pd.read_csv("output.csv", sep=",")
#le = preprocessing.LabelEncoder()

#le.fit(data['price'])
#le.transform(data['price'])

#data.values[:,:-1].astype(float32)

data['price'].replace('%','',regex=True).astype('float')/100
data['carYear'].replace('%','',regex=True).astype('float')/100


price = data['price'][:, np.newaxis]
carYear  = data['carYear']


lr = LinearRegression()
lr.fit(price, carYear)

b_0   = lr.intercept_
coeff = lr.coef_