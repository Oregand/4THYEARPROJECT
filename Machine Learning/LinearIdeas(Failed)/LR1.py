__author__ = 'davidoregan'

from scipy import stats
from pylab import *
from numpy import *

import pandas as pd
import numpy as np
dat = pd.read_csv('carData.csv')
np.corrcoef(dat)


#data= matplotlib.mlab.csv2rec('carData.csv',delimiter=',')
#data = loadtxt("carData.csv")
#data = genfromtxt('carData.csv', delimiter=';')[:,:-1]
#data = genfromtxt('carData.csv')


xi = arange(0,9)
A = array([ xi, ones(9)])
# linearly generated sequence
y = [data['mileage'][0], 20, 20.5, 21.5, 22, 23, 23, 25.5, 24]





slope, intercept, r_value, p_value, std_err = stats.linregress(xi,y)

print 'r value', r_value
print  'p_value', p_value
print 'standard deviation', std_err

line = slope*xi+intercept
plot(xi,line,'r-',xi,y,'o')
show()