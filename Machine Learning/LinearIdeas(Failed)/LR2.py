import numpy as np
from pylab import plot,show
from scipy import stats


import pandas as pd
dat = pd.read_csv('carData.csv')
np.corrcoef(dat)

#my_data = genfromtxt('carData.csv', delimiter=',')

dat[dat=='']='0'
a2 = dat.astype(np.float)

xi = np.arange(0,9)
A = np.array([ xi, np.ones(9)])
# linearly generated sequence
y = [19, 20, 20.5, 21.5, 22, 23, 23, 25.5, 24]

slope, intercept, r_value, p_value, std_err = stats.linregress(xi,y)

print 'r value', r_value
print  'p_value', p_value
print 'standard deviation', std_err

line = slope*xi+intercept
plot(xi,line,'r-',xi,y,'o')
show()