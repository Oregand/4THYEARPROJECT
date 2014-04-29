__author__ = 'davidoregan'


import time                     # Imports system time module to time your script
from pylab import *             # Imports numpy, scipy, and matplotlib etc.
from scipy import stats as st
import csv                      # Imports .csv file reader
close('all')  # close all open figures

# Read in small data from .csv file
# Filepath
#filepath = '../'
# In windows you can also specify the absolute path to your data file
# filepath = 'C:/Dropbox/Towson/Teaching/3_ComputationalEconomics/Lectures/Lecture4/'



# ------------- Load data --------------------
data =[]  # Define empty list for data reading
for row in csv.reader(open("MiscIdeas/../MiscIdeas/carData.csv"), delimiter=','):
    data.append(row)    # read data row by row

# Let's have a look at it, it's a nested list
data


# Split data into header and values
header      = data[0]        # first row contains headers of data
print header
groupNv     = []
groupv      = arange(1,6,1)  # make a vector from 1,2,...,5
freqv       = zeros((5,1),float)
for i in range(1,6):
    print i
    freqv[i-1]  = data[i][1]
    groupNv.append(data[i][0])