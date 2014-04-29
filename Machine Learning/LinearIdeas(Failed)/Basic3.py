__author__ = 'davidoregan'


import scipy
import numpy
from pybrain.datasets            import ClassificationDataSet
from pybrain.utilities           import percentError
from pybrain.tools.shortcuts     import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure.modules   import SoftmaxLayer
from sklearn.metrics             import precision_score,recall_score,confusion_matrix
def makeDataset(CSVfile,ClassFile):
    #import the features to data, and their classes to dataClasses
    data=numpy.genfromtxt(CSVfile,delimiter=",")
    classes=numpy.genfromtxt(ClassFile,delimiter=",")
    print("Building the dataset from CSV files")
    #Initialize an empty Pybrain dataset, and populate it
    alldata=ClassificationDataSet(len(data[0]),1,nb_classes=3)
    for count in range(len((classes))):
        alldata.addSample(data[count],[classes[count]])
    return alldata



def makeNeuralNet(alldata,trainingPercent=.3,hiddenNeurons=5,trainingIterations=20):
    #Divide the data set into training and non-training data
    testData, trainData = alldata.splitWithProportion(trainingPercent)
    testData._convertToOneOfMany( )
    trainData._convertToOneOfMany( )
    #Then build the network, and using backwards propogation to train it
    network = buildNetwork( trainData.indim, hiddenNeurons, trainData.outdim, outclass=SoftmaxLayer )
    trainer = BackpropTrainer( network, dataset=trainData, momentum=0.1, verbose=True, weightdecay=0.01)
    for i in range(trainingIterations):
        print("Training Epoch #"+str(i))
        trainer.trainEpochs( 1 )
    return [network,trainer]



def checkNeuralNet(trainer,alldata):
    predictedVals=trainer.testOnClassData(alldata)
    actualVals=list(alldata['target'])
##    for row in alldata['target']:
##        row=list(row)
##        index=row.index(1)
##        actualVals+=[index]
    print("-----------------------------")
    print("-----------------------------")
    print("The precision is "+str(precision_score(actualVals,predictedVals)))
    print("The recall is "+str(recall_score(actualVals,predictedVals)))
    print("The confusion matrix is as shown below:")
    print(confusion_matrix(actualVals,predictedVals))


CSVfile="carData.csv"
ClassFile="carData.csv"
#Build our dataset
alldata=makeDataset(CSVfile,ClassFile)
#Build and train the network
net=makeNeuralNet(alldata,trainingPercent=.7,hiddenNeurons=20,trainingIterations=20)
network=net[0]
trainer=net[1]
#Check it's strength
checkNeuralNet(trainer,alldata)