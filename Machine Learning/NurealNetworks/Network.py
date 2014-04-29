__author__ = 'davidoregan'

from pybrain.structure import FeedForwardNetwork
from pybrain.structure import LinearLayer, SigmoidLayer
from pybrain.structure import FullConnection
from pybrain.structure import RecurrentNetwork


#Specifiy networks
n = FeedForwardNetwork()
r = RecurrentNetwork()


LinearLayer(2, name="Nigger")
inLayer = LinearLayer(2)
hiddenLayer = SigmoidLayer(3)
outLayer = LinearLayer(1)

n.addInputModule(inLayer)
n.addModule(hiddenLayer)
n.addOutputModule(outLayer)

in_to_hidden = FullConnection(inLayer, hiddenLayer)
hidden_to_out = FullConnection(hiddenLayer, outLayer)

n.addConnection(in_to_hidden)
n.addConnection(hidden_to_out)

n.sortModules()


r.addInputModule(LinearLayer(2, name='in'))
r.addModule(SigmoidLayer(3, name='hidden'))
r.addOutputModule(LinearLayer(1, name='out'))
r.addConnection(FullConnection(n['in'], n['hidden'], name='c1'))
r.addConnection(FullConnection(n['hidden'], n['out'], name='c2'))

r.addRecurrentConnection(FullConnection(n['hidden'], n['hidden'], name='c3'))

r.sortModules()

#Show trainable weights
print "These are the trainable weights"
print in_to_hidden.params
print hidden_to_out.params

#Test Prints
print n.activate([1, 2])
print n

print ""

print r.activate((2, 2))
print r
