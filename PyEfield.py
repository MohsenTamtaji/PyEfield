from numpy import exp, random, dot
import numpy as np
import pickle
import matplotlib.pyplot as plt
import os

r=[[7/100]] #Define the diameter of gold nanospere in nm. For example 7 nm
Shape=2 # Define the shape of nanoparticle 1 means nanopsphere and 2 means nanocube

TrainingNumber=np.size(r)
class NeuronLayer():
    def __init__(self, number_of_neurons, number_of_inputs_per_neuron):
        self.synaptic_weights = 2 * random.random((number_of_inputs_per_neuron, number_of_neurons)) - 1
class NeuralNetwork():
    def __sigmoid(self, x):
        return 1 / (1 + exp(-x))

    def __sigmoid_derivative(self, x):
        return x * (1 - x)

    def think(self, inputs):
        output_from_layer1 = self.__sigmoid(dot(inputs, self.layer1.synaptic_weights))
        output_from_layer2 = self.__sigmoid(dot(output_from_layer1, self.layer2.synaptic_weights))
        return output_from_layer1, output_from_layer2
if Shape==1:
    pickle_in=open("TNNEfield1.pickle","rb")
elif Shape==2:
    pickle_in=open("TNNEfield2.pickle","rb")
else:
    print('Define the shape of nanoparticle correctly and re-run: 1 stands for nanopsphere and 2 stands for nanocube')
    os._exit(0)
neural_network2=pickle.load(pickle_in)
n, output = neural_network2.think(r)
meshcellsx=501
x,y,EE = np.zeros((meshcellsx, meshcellsx)),np.zeros((meshcellsx, meshcellsx)),np.zeros((meshcellsx, meshcellsx))
for TrainingData in range(TrainingNumber):
    jj = 0
    for i in range(meshcellsx):
        for j in range(meshcellsx):
            x[i][j] = (i  - 250) / 250  * 4 * r[TrainingData][0]
            y[i][j] = (j  - 250) / 250  * 4 * r[TrainingData][0]
            EE[i][j] = output[TrainingData][jj]
            jj += 1
    EE = EE * 10
    #EE[1][1] = 2.0**1
    EE[0][0] = 0
    plt.figure()
    CS=plt.contourf(y, x, EE, 500, cmap='jet',vmin=0,vmax=2)
    plt.clim(0, 1.5)
    plt.colorbar(CS)
    plt.xlabel('x (nm)')
    plt.ylabel('y (nm)')
    plt.text(0,0,'Au')
    plt.text(0, 0, 'Au', fontsize=14,fontweight='bold', color='white')
    plt.text(0, r[TrainingData][0]*2, 'SiO$_2$', fontsize=14,fontweight='bold', color='white')
    plt.show()
