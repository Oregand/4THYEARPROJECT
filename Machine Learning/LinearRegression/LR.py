__author__ = 'davidoregan'


# Import my libarys
import re
import csv
import pandas.io.sql as psql
import json
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LinearRegression
from sklearn import svm
from yhat import BaseModel, YhatModel
import MySQLdb
from pylab import *
from numpy import *


# Notes

#  DELETE FROM bar WHERE col1 LIKE '%foo%' OR col2 LIKE '%foo%'....etc
# DELETE FROM `bmw_3` WHERE `price` LIKE '%POA%'
# Golf worked best with LR
# SELECT * FROM `audi_a4` WHERE `mileage` = ""
# UPDATE `CarDealz` SET `mileage` = REPLACE(`mileage`, '.', ' ')





# --------------------------------------------------------------------------------------------------------

# connect to my DB to get data, place data into a pandas Dataframe
db = MySQLdb.connect(host="mysql.raven.com", user="david", passwd="apUJP5VxBTZ9atXD", port=3306,
                     db="david")
sql = """
        select *
            from t_corolla
      """
df = psql.frame_query(sql, db)
# db.close()




# Do some basic file editing to make my data work with algorithm
# -------------------Training Set Management(From DB)------------------------------------------------

df['mileage'] = df['mileage'].str.replace('M', '')
df['mileage'] = df['mileage'].str.replace(',', '')
df['mileage'] = df['mileage'].astype('float')

age = 2014 - df['carYear']
df['carYear'] = age

df['price'] = df['price'].str.replace(',', '')
# df['price'] = df['price'].str.replace('POA', '1')
df['price'] = df['price'].astype('float64')


# --------------------------------------------------------------------------------------------------------
# Now we need to edit our dataset some more
# The reason for this is cases for accuracy
# Example - New cars dont require a NCT, nor should they have any mileage
# Given this, these features should make those cars more valuable,not less




# Colours - red,blue,silver,white,black
df['Colour'] = df['Colour'].str.replace('.*Grey.*', 'Grey')
df['Colour'] = df['Colour'].str.replace('.*Red.*', 'Red')
df['Colour'] = df['Colour'].str.replace('.*White.*', 'White')
df['Colour'] = df['Colour'].str.replace('.*Blue.*', 'Blue')
df['Colour'] = df['Colour'].str.replace('.*Black.*', 'Black')
df['Colour'] = df['Colour'].str.replace('.*Silver.*', 'Silver')


# Instead of 32 counties, make dublin/lensiter/msuter/ulster

# Lensister
df['location'] = df['location'].str.replace('Louth', 'Leinster')
df['location'] = df['location'].str.replace('Meath', 'Leinster')
df['location'] = df['location'].str.replace('Longford', 'Leinster')
df['location'] = df['location'].str.replace('Westmeath', 'Leinster')
df['location'] = df['location'].str.replace('Offaly', 'Leinster')
df['location'] = df['location'].str.replace('Kildare', 'Leinster')
df['location'] = df['location'].str.replace('Laois', 'Leinster')
df['location'] = df['location'].str.replace('Wicklow', 'Leinster')
df['location'] = df['location'].str.replace('Carlow', 'Leinster')
df['location'] = df['location'].str.replace('Kilkenny', 'Leinster')
df['location'] = df['location'].str.replace('Wexford', 'Leinster')


# Ulster
df['location'] = df['location'].str.replace('Derry', 'Ulster')
df['location'] = df['location'].str.replace('Antrim', 'Ulster')
df['location'] = df['location'].str.replace('Down', 'Ulster')
df['location'] = df['location'].str.replace('Armagh', 'Ulster')
df['location'] = df['location'].str.replace('Monaghan', 'Ulster')
df['location'] = df['location'].str.replace('Tyrone', 'Ulster')
df['location'] = df['location'].str.replace('Fermanagh', 'Ulster')
df['location'] = df['location'].str.replace('Donegal', 'Ulster')
df['location'] = df['location'].str.replace('Cavan', 'Ulster')

# Munster
df['location'] = df['location'].str.replace('Clare', 'Munster')
df['location'] = df['location'].str.replace('Limerick', 'Munster')
df['location'] = df['location'].str.replace('Tipperary', 'Munster')
df['location'] = df['location'].str.replace('Waterford', 'Munster')
df['location'] = df['location'].str.replace('Cork', 'Munster')
df['location'] = df['location'].str.replace('Kerry', 'Munster')


# Connatch
df['location'] = df['location'].str.replace('Galway', 'Connucht')
df['location'] = df['location'].str.replace('Sligo', 'Connucht')
df['location'] = df['location'].str.replace('Mayo', 'Connucht')
df['location'] = df['location'].str.replace('Leitrim', 'Connucht')
df['location'] = df['location'].str.replace('Roscommon', 'Connucht')



# NCT
# For this we need three categories, NCT Needed - present/ NCT Needed - Not present/ NCT Not Needed(New car) - Not present






# --------------------------------------------------------------------------------------------------------


# Fill in any empy spaces as 0
df.fillna(0, inplace=True)


# --------------------------------------------------------------------------------------------------------

# Edit our dataframe to drop colums we dont need and seperate the price colum already there
df_noID = df.drop(['ID'],1)
df_no_priceLinkTitle = df.drop(['ID', 'price', 'link', 'title'], 1)


# --------------------------------------------------------------------------------------------------------


#Now use the sklearn DictVectorizor libary to map each colum from the data frame into a numpy array
# Transforms lists of feature-value mappings to vectors.
dv = DictVectorizer()
dv.fit(df.T.to_dict().values())


# --------------------------------------------------------------------------------------------------------
# We specifiy a LR model to predict a price for each unique feature from our DictV


# Create linear regression object
LR = LinearRegression()

# Train the model using the training sets(DataFrame without title, link or price and then price by itself)
# Model is trained to fit a price against a feature
LR = LR.fit(dv.transform(df_no_priceLinkTitle.T.to_dict().values()), df.price)

print LR

# Print the model in format native to python
print ' + '.join([format(LR.intercept_, '0.2f')])

# Print the model via python format
# Create a map for the feature names and the corressponding estimated coefficients for the linear regression problem
# Done using map & lambda
print map(lambda (a, b): "(%0.2f %s)" % (b, a), zip(dv.feature_names_, LR.coef_))

# Support Vector Machine

clf = svm.SVC()

clf = clf.fit(dv.transform(df_no_priceLinkTitle.T.to_dict().values()), df.price)


# Explained variance score: 1 is perfect prediction
print ('Variance score LR: %.2f' % LR.score(dv.transform(df_no_priceLinkTitle.T.to_dict().values()), df.price))

print ('Variance score SVM: %.2f' % clf.score(dv.transform(df_no_priceLinkTitle.T.to_dict().values()), df.price))

# --------------------------------------------------------------------------------------------------------


# Set variable to hold good deal check
goodDeal = ''


class predictFunction(BaseModel):


    # Transform takes dictVectoiser
    # DictVect is transformed into sparse matrix
    # Return the transformed matrix
    def transform(self, dict):
        return self.dv.transform(dict)

    # info is our input vector(car information)
    # Predicted price is what our model determines based on the LR
    def predict(self, info):

        # Transform numpy array back into back into features
        dict = self.dv.inverse_transform(info)[0]

        # predicted is the final variable from our LR model per car
        predicted = self.lr.predict(info)[0]

        # Evaluate if its a good deal vs asking price from ad
        goodDeal = (dict['price'] < predicted)


        # Return iteritem of each dict section,
        # This is dont over dict.items to avoid a long and wasteful item tuple
        return {'predictedPrice': str(round(predicted)),
                "title": [(k, v) for (k, v) in dict.iteritems() if 'title' in k],
                'link': [(k, v) for (k, v) in dict.iteritems() if 'link' in k],
                'carYear': [(k, v) for (k, v) in dict.iteritems() if 'carYear' in k],
                'mileage': [(k, v) for (k, v) in dict.iteritems() if 'mileage' in k],
                'Owners': [(k, v) for (k, v) in dict.iteritems() if 'Owners' in k],
                'location': [(k, v) for (k, v) in dict.iteritems() if 'location' in k],
                'Colour': [(k, v) for (k, v) in dict.iteritems() if 'Colour' in k],
                'askingPrice': dict['price'],
                'difference': round(predicted - dict['price']),
                'GoodDeal': str(goodDeal),
        }

# --------------------------------------------------------------------------------------------------------

# Start by passing our variables(transformed data frame and LR model to function above)
# Open a json file for output
# Display the predicted price as well as our car variables from our LR model earlier
# Store info in json file



predictedPrice = predictFunction(dv=dv, lr=LR)
print " "
with open('bmw_3.json', 'w') as outfile:
    for i in range(20):
        outputPrice = predictedPrice.predict(predictedPrice.transform(df_noID.T.to_dict()[i]))
        # print outputPrice[0]
        json.dump(outputPrice, outfile)
        outfile.write('\n')

# --------------------------------------------------------------------------------------------------------
# Write Json data to csv for db insert

data = []
with open('bmw_3.json') as f:
    for line in f:
        data.append(json.loads(line))
print data[0]

f = csv.writer(open('Dealz.csv', 'wb+'))
# use encode to convert non-ASCII characters
for item in data:
    # values = [x.encode('utf8') for x in it;em['Predicted Difference:'].values()]
    f.writerow(
        [str(item['title'])[10:60], str(item['link'])[9:92], item['askingPrice'], item['predictedPrice'], item['difference'], str(item['carYear'])[14:15], str(item['location'])[13:21],(item['mileage'])[14:20], str(item['Colour'])[11:17] ,str(item['Owners'])[13:14], item['GoodDeal']])

# --------------------------------------------------------------------------------------------------------


#Open database connection
# prepare a cursor object using cursor() method
cursor = db.cursor()

#SQL query to INSERT a record into the table.
for item in data:

    make = str(item['title'])[10:60]
    URL = str(item['link'])[9:92].strip()
    askingPrice = str(item['askingPrice'])
    difference = str(item['difference'])
    carAge = str(item['carYear'])[14:15]
    location = str(item['location'])[13:21]
    mileage = str(item['mileage'])[13:20]
    colour = str(item['Colour'])[11:17].strip()
    owners = str(item['Owners'])[13:14]


    # l = re.sub(r'^"|"$', '', l)

    location = re.sub(r'[^\w]', ' ', location)
    colour = re.sub(r'[^\w]', ' ', colour)

    if item['GoodDeal'] == 'True':
        cursor.execute('''INSERT into CarDealz (title, link, askingPrice, predictedPrice, difference, carYear, location, mileage, Colour, Owners)
                                values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''',
                       (
                           make,
                           URL,
                           askingPrice,
                           item['predictedPrice'],
                           difference,
                           carAge,
                           location,
                           mileage,
                           colour,
                           owners))

# Commit your changes in the database
db.commit()

# disconnect from server
db.close()


# --------------------------------------------------------------------------------------------------------











