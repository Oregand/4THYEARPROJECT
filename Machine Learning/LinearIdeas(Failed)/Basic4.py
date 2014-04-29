__author__ = 'davidoregan'

import numpy


def get_dataset():

    array = numpy.loadtxt('carData.csv', delimiter=',', skiprows=1)

    # assume last field in csv is single target variable
    # and all other fields are input variables
    number_of_columns = array.shape[1]
    dataset = SupervisedDataSet(number_of_columns - 1, 1)

    print array[0]
    #print array[:,:-1]
    #print array[:,-1]
    #dataset.addSample(array[:,:-1], array[:,-1])
    #dataset.addSample(array[:,:-1], array[:,-2:-1])
    dataset.setField('input', array[:,:-1])
    dataset.setField('target', array[:,-1:])

    return dataset

print get_dataset()