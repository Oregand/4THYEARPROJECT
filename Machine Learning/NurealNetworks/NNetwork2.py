__author__ = 'davidoregan'


''' First we import a bunch of shit '''

from pybrain.datasets import ClassificationDataSet
from pybrain.utilities import percentError
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure.modules import SoftmaxLayer

from pylab import ion, ioff, figure, draw, contourf, clf, show, hold, plot
from scipy import diag, arange, meshgrid, where
from numpy.random import multivariate_normal

''' PyBrain uses several dataset classes to make data handling easier (or not). For a classification problem, we will use the ClassificationDataSet. This dataset has two classes: 0 & 1;. The groups are clearly distinct.

In the declaration: 2 = dimensionality of the each input vector; 1 = number of output types; nb_classes = number of classes. '''

alldata = ClassificationDataSet(2, 1, nb_classes=2)
alldata.addSample([-1,-1],[0])
alldata.addSample([-1,-1],[0])
alldata.addSample([-1,-1],[0])
alldata.addSample([-1,-1],[0])
alldata.addSample([-1,-1],[0])

alldata.addSample([1,1],[1])
alldata.addSample([1,1],[1])
alldata.addSample([1,1],[1])
alldata.addSample([1,1],[1])
alldata.addSample([1,1],[1])

''' Once the dataset has been created, we split it into a training and test set:

 '''

tstdata, trndata = alldata.splitWithProportion( 0.25 )
trndata._convertToOneOfMany( )
tstdata._convertToOneOfMany( )

#We can also examine the dataset
print "Number of training patterns: ", len(trndata)
print "Input and output dimensions: ", trndata.indim, trndata.outdim
print "First sample (input, target, class):"
print trndata['input'][0], trndata['target'][0], trndata['class'][0]

''' Now lets build a neural network and train it using a back propagation network on the training data (trndata).

'''

fnn = buildNetwork( trndata.indim, 5, trndata.outdim, recurrent=False )
trainer = BackpropTrainer( fnn, dataset=trndata, momentum=0.1, verbose=True, weightdecay=0.01 )

''' Originally I figured the best way to train was to do it myself, having looked at my code, and that in the doc, I think that it’s best to use the built-in functions:
'''


from pybrain.tools.neuralnets import NNregression, Trainer
# Create you dataset - as above
nn = NNregression(alldata)
nn.setupNN()
nn.runTraining()

''' Train the network for n epochs '''

# I am not sure about this, I don't think my production code is implemented like this
modval = ModuleValidator()
for i in range(1000):
      trainer.trainEpochs(1)
      trainer.trainOnDataset(dataset=trndata)
      cv = CrossValidator( trainer, trndata, n_folds=5, valfunc=modval.MSE )
      print "MSE %f @ %i" %( cv.validate(), i )

''' Now predict the test data again – this should really be a HOT set.

 '''


print tstdata
print ">", trainer.testOnClassData(dataset=tstdata)