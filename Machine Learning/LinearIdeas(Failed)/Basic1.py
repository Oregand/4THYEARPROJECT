__author__ = 'davidoregan'

from pylab import *


data= matplotlib.mlab.csv2rec('carData.csv',delimiter=',')

print data['title']
print " "
print data['link']


bar(arange(len(data)), data('price'), color='red', width=0.1, label='price')
bar(arange(len(data)), data('mileage'), color='blue', width=0.1, label='mileage')

xticks(range(len(data)), data['price'])

legend()

grid('.')

title('Simple grid price and mileage')