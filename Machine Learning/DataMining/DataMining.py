__author__ = 'davidoregan'


import pandas as pd
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LinearRegression
from yhat import BaseModel
import matplotlib.pyplot as plt
import scipy as sp


import warnings
warnings.filterwarnings('ignore')
pd.options.display.width = 900


# Open my training file, 1400 lines

training = pd.read_csv('wv_golfTraining.csv')
print training.shape

# Read my test file, 100 lines

testing = pd.read_csv('wv_golf.csv')
print testing.shape


# Do some basic file editing to make my data work with algorithm

training['mileage'] = training['mileage'].str.replace('M', '')
training['mileage'] = training['mileage'].str.replace(',', '')
training['price'] = training['price'].str.replace(',', '')
training['price'] = training['price'].str.replace('POA', '0')
training['mileage'] = training['mileage'].astype('float64')
training['price'] = training['price'].astype('float64')

testing['mileage'] = testing['mileage'].str.replace('M', '')
testing['mileage'] = testing['mileage'].str.replace(',', '')
testing['price'] = testing['price'].str.replace(',', '')
testing['price'] = testing['price'].str.replace('POA', '0')
testing['mileage'] = testing['mileage'].astype('float64')
testing['price'] = testing['price'].astype('float64')




# Fill in any empy spaces as 0

training.fillna(0, inplace=True)
testing.fillna(0, inplace=True)
#training.values[:,:-1].astype(float)

training_no_price = training.drop(['price'], 1)
print training_no_price.head()

training_no_priceLink = training_no_price.drop(['link'], 1)
print training_no_priceLink

training_no_priceLinkTitle = training.drop(['price','link','title'],1)
print training_no_priceLinkTitle

# -----------------------------------------


testing_no_priceLinkTitle = testing.drop(['price','link','title'],1)
print testing_no_priceLinkTitle

# -----------------------------------------


dv = DictVectorizer()
dv.fit(training_no_priceLinkTitle.T.to_dict().values())
print dv


# -----------------------------------------


print len(dv.feature_names_)
print dv.feature_names_

# -----------------------------------------


LR = LinearRegression().fit(dv.transform(training_no_priceLink.T.to_dict().values()), training.price)
LR2 = ' + '.join([format(LR.intercept_, '0.2f')] + map(lambda (f,c): "(%0.2f %s)" % (c, f), zip(dv.feature_names_, LR.coef_)))

print LR2
# -----------------------------------------



trainingErrs = abs(LR.predict(dv.transform(training.T.to_dict().values())) - training.price)

errorP = sp.percentile(trainingErrs, [75, 90, 95, 99])

print errorP

outlierIdx = trainingErrs >= sp.percentile(trainingErrs, 95)

#plt.scatter(training.mileage, training.price, c=(0,0,1), marker='s')
#plt.scatter(training.mileage[outlierIdx], training.price[outlierIdx], c=(1,0,0), marker='s')



errs = abs(LR.predict(dv.transform(testing.T.to_dict().values())) - testing.price)
# plt.hist(errs, bins=50)
#
#
# # outlierIdx = trainingErrs
# plt.scatter(training.mileage, training.price, c=(0,0,1), marker='s')
# plt.scatter(training.mileage[outlierIdx], training.price[outlierIdx], c=(1,0,0), marker='s')
# plt.show()


class PricingModel(BaseModel):

    #Place transformed data into numpy array for use
    def transform(self, doc):
        return self.dv.transform(doc)


    def predict(self, x):
        """
        Evaluate model on array
        delegates to LinearRegression self.lr
        returns a dict (will be json encoded) suppling
        "predictedPrice", "suspectedOutlier", "x", "threshold"
        where "x" is the input vector and "threshold" is determined
        whether or not a listing is a suspected outlier.
        """
        doc = self.dv.inverse_transform(x)[0]
        predicted = self.lr.predict(x)[0]
        err = abs(predicted)
        return {'predictedPrice': predicted,
                'x': doc,
                'suspectedOutlier': 1 if (err > self.threshold) else 0,
                'threshold': self.threshold}

pm = PricingModel(dv=dv, lr=LR, threshold=sp.percentile(trainingErrs, 95))
print " "

for i in range(10):
    print pm.predict(pm.transform(testing.T.to_dict()[i]))




