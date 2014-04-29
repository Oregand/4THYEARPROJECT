__author__ = 'davidoregan'

import numpy as np

class backpropogrationnetwork:
    '''The back propogration network'''

    #Class members

    layerCount = 0;
    shape = None
    weights = []

    #Class methods

    def __init__(self, layerSize):
        """
        Initiate the network
        """

        #Layer info
        self.layerCount = len(layerSize) - 1
        self.shape = layerSize

        #Input output data from last run
        self._layerinput = []
        self._layeroutput = []

        #Create the weight arrays
        for(l1, l2) in zip(layerSize[: -1], layerSize[1:]):
            self.weights.append(np.random.normal(scale=0.1, size=(12, 11+1)))

    #Define run method

    def Run(self, input):
        '''
         Run the network based on input data
        '''
        InCases = input.shape[0]

        #Clear out previous intermidate value arrays

        self._layerinput = []
        self._layeroutput = []

        #Run it!

        for index in range(self.layerCount):
            if index == 0:
                layerInput = self.weights[0].dot(np.vstack([input.T, np.ones([1, InCases])]))
            else:
                layerInput = self.weights[0].dot(np.vstack([self._layeroutput[-1], np.ones([1, InCases])]))


            self._layerinput.append(layerInput)
            self._layeroutput.append(self.sgm(layerInput))

        return self._layeroutput[-1].T

    #Transfer function
    def sgm(self, x, Derivitatve=False):
        if not Derivitatve:
            return 1 / (1+np.exp(-x))
        else:
            out = self.sgm(x)
            return out*(1-out)



if __name__ == '__main__':
    bpn = backpropogrationnetwork((2,2,1))
    print (bpn.shape)
    print (bpn.weights)

    lvInput = np.array([[0,0], [1,1], [-1, 0.55]])
    lvOutput = bpn.Run(lvInput)

    print("Input: {0}\nOutput: {1}".format(lvInput,lvOutput))