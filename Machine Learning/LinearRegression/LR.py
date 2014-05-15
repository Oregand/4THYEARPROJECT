__author__ = 'davidoregan'


# Import my libarys
import pandas as pd
import re
import csv
import pandas.io.sql as psql
import json
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LinearRegression
from sklearn import svm
from yhat import BaseModel
import MySQLdb




# --------------------------------------------------------------------------------------------------------

# connect to my DB to get data, place data into a pandas Dataframe
db = MySQLdb.connect(host="mysql.raven.com", user="david", passwd="apUJP5VxBTZ9atXD", port=3306,
                     db="david")
sql = """
        select *
            from vw_golf
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

# # NCT Needed - Not Present
# if df['NCT'].empty & age >= 1:
#     df['NCT'] = df['NCT'].str.replace('', 'YOLO')
# print df['NCT']





# --------------------------------------------------------------------------------------------------------


# Fill in any empy spaces as 0
df.fillna(0, inplace=True)


# --------------------------------------------------------------------------------------------------------

# Edit our dataframe to drop colums we dont need and seerate the price colum already there

df_no_price = df.drop(['price'], 1)
df_no_priceLink = df_no_price.drop(['link'], 1)
df_no_priceLinkTitle = df.drop(['ID', 'price', 'link', 'title'], 1)

df_no_IDLinkTitle = df.drop(['ID', 'link', 'title'], 1)

df_no_ID = df.drop(['ID'], 1)

# rows_with_strings  = df.apply(lambda row :any([ isinstance(e, 'POA') for e in row ]), axis=1)
# df_no_ID = df_no_ID[~rows_with_strings]
# df_no_ID = df_no_ID[df_no_ID.price != 0]
# df = df[df.price != 0]
# df_no_ID = df_no_ID[df_no_ID.isin(df_no_IDLinkTitle.to_dict(outtype='price')).all('POA')]
# df_no_ID.fillna(0, inplace=True)




# --------------------------------------------------------------------------------------------------------


#Now use the sklearn DictVectorizor libary to map each colum from the data frame into a numpy array
# Transforms lists of feature-value mappings to vectors.
#
#
dv = DictVectorizer()
dv.fit(df.T.to_dict().values())


# --------------------------------------------------------------------------------------------------------

# Create linear regression object
LR = LinearRegression()

# Train the model using the training sets(DataFrame without title, link or price and then price by itself)
LR = LR.fit(dv.transform(df_no_priceLinkTitle.T.to_dict().values()), df.price)

print LR
print ' + '.join([format(LR.intercept_, '0.2f')] + map(lambda (f,c): "(%0.2f %s)" % (c, f), zip(dv.feature_names_, LR.coef_)))

clf = svm.SVC()

clf = clf.fit(dv.transform(df_no_priceLinkTitle.T.to_dict().values()), df.price)



# Explained variance score: 1 is perfect prediction
print ('Variance score: %.2f' % LR.score(dv.transform(df_no_priceLinkTitle.T.to_dict().values()), df.price))

print ('Variance score: %.2f' % clf.score(dv.transform(df_no_priceLinkTitle.T.to_dict().values()), df.price))


# --------------------------------------------------------------------------------------------------------

# Predict function that uses yhat's basemodel
# This function allows me to use the transform method
#  This will map my input to the numpy array needed by the LR model
#  The predict function will then evaluate my LR model based on the numpy array

goodDeal = ''


class predictFunction(BaseModel):
    #Place transformed data into numpy array for use
    def transform(self, doc):
        return self.dv.transform(doc)


    # x is our input vector(car information)
    #Predicted price is what our model determines based on the LR
    def predict(self, x):
        doc = self.dv.inverse_transform(x)[0]
        predicted = self.svm .predict(x)[0]

        # err = abs(predicted - doc['price'])

        goodDeal = (doc['price'] < predicted)

        return {'predictedPrice': str(round(predicted)),
                # 'Details': doc,
                "title" : [(k, v) for (k, v) in doc.iteritems() if 'title' in k],
                'link' : [(k, v) for (k, v) in doc.iteritems() if 'link' in k],
                'location' : [(k, v) for (k, v) in doc.iteritems() if 'location' in k],
                'Colour' : [(k, v) for (k, v) in doc.iteritems() if 'Colour' in k],
                'Asking Price' : doc['price'],
                # 'predictedDifference': err,
                'GoodDeal': str(goodDeal),
        }


# --------------------------------------------------------------------------------------------------------
# Now we need to vailidate if the cars are actually a good deal i.e.
# - If asking price is less than predicted price(good deal) else bad deal




# --------------------------------------------------------------------------------------------------------

# Start by passing our variables(transformed data frame and LR model to function above)
# Open a json file for output
# Display the predicted price as well as our car variables from our LR model earlier
# Store info in json file



predictedPrice = predictFunction(dv=dv, svm=clf)
print " "
with open('vw_golfDealz.json', 'w') as outfile:
    for i in range(200):
        outputPrice = predictedPrice.predict(predictedPrice.transform(df_no_ID.T.to_dict()[i]))
        # print outputPrice[0]
        json.dump(outputPrice, outfile)
        outfile.write('\n')


# --------------------------------------------------------------------------------------------------------
# Write Json data to csv for db insert

data = []
with open('vw_golfDealz.json') as f:
    for line in f:
        data.append(json.loads(line))
print 'yolo'
print data[0]

f = csv.writer(open('Dealz.csv', 'wb+'))
# use encode to convert non-ASCII characters
for item in data:
    # values = [x.encode('utf8') for x in it;em['Predicted Difference:'].values()]
    f.writerow([item['predictedPrice'], item['GoodDeal'], str(item['title'])[7:35], str(item['link'])[9:99]])


# --------------------------------------------------------------------------------------------------------
# #Open database connection
# prepare a cursor object using cursor() method
cursor = db.cursor()

#SQL query to INSERT a record into the table FACTRESTTBL.
for item in data:

    t = str(item['title'])[10:35]
    l = str(item['location'])[13:21]
    c = str(item['Colour'])[11:17].strip()


    # l = re.sub(r'^"|"$', '', l)

    l = re.sub(r'[^\w]', ' ', l)
    c = re.sub(r'[^\w]', ' ', c)

    if item['GoodDeal'] == 'True':
        cursor.execute('''INSERT into dealz2 (title, link ,location  ,Colour, predictedPrice, GoodDeal)
                                values (%s, %s, %s, %s, %s, %s)''',
                            (
                            t,
                            str(item['link'])[9:99].strip(),
                            l,
                            c,
                            item['predictedPrice'],
                            item['GoodDeal']))

# Commit your changes in the database
db.commit()

# disconnect from server
db.close()


# --------------------------------------------------------------------------------------------------------











