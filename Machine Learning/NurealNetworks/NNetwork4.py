__author__ = 'davidoregan'


from pybrain.datasets            import *
from pybrain.utilities           import percentError
from pybrain.tools.shortcuts     import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure.modules   import SoftmaxLayer

ds = SupervisedDataSet(6,3)

tf = open('MiscIdeas/../MiscIdeas/carData.csv','r')

for line in tf.readlines():
    data = [float(x) for x in line.strip().split(',') if x != '']
    indata =  tuple(data[:6])
    outdata = tuple(data[6:])
    ds.addSample(indata,outdata)

n = buildNetwork(ds.indim,8,8,ds.outdim,recurrent=True)
t = BackpropTrainer(n,learningrate=0.01,momentum=0.5,verbose=True)
t.trainOnDataset(ds,1000)
t.testOnData(verbose=True)