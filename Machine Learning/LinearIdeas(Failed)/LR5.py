__author__ = 'davidoregan'

import numpy as np
from pylab import plot,show
from scipy import stats
import csv
import pandas as pd


#Load csv into pandas dataframe
df = np.loadtxt('output.csv', comments='#', delimiter=',', skiprows=1, usecols=(3,))



xi = np.arange(0,9)
A = np.array([ xi, np.ones(9)])
# linearly generated sequence
y = [df['price'][0], df['price'][1], df['price'][2], df['price'][3], df['price'][4], df['price'][5], df['price'][6], df['price'][7], df['price'][8]]

slope, intercept, r_value, p_value, std_err = stats.linregress(xi,y)

print 'r value', r_value
print  'p_value', p_value
print 'standard deviation', std_err

line = slope*xi+intercept
plot(xi,line,'r-',xi,y,'o')
show()