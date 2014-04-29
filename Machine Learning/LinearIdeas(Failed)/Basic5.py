__author__ = 'davidoregan'

from pylab import *


data= matplotlib.mlab.csv2rec('carData.csv',delimiter=',')

print data['title']
print " "
print data['link']

pie(data['mileage'], label='mileage')