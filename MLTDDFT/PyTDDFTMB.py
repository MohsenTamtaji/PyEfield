import numpy as np
import pickle
import matplotlib.pyplot as plt
from molmod import *
import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

Location=r"E:\SOSAC\Gaussian\2\MB\MLTDDFT" #Define the location of your files
E=0.2 #(V/A) put the intensity of field in Volt/Angstrom. the range is in +- 0.271 V/A.

Property=np.zeros((1,1))
Property[0,0]=(E+0.257)/(2*0.257) #normalizing
filename = '\PyTDDFTMB2.sav'
loaded_model = pickle.load(open(Location+filename, 'rb'))
output=loaded_model.predict(Property)
print('E=',np.round(E,3),' V/A')
print('HOMO=',np.round(output[0][0],3),' eV')
print('LUMO=',np.round(output[0][1],3),' eV')
print('L-H=',np.round(output[0][1]-output[0][0],3),' eV')
print('S1-S0=',np.round(output[0][3],3),' eV')
print('S2-S0=',np.round(output[0][4],3),' eV')
print('T1-S0=',np.round(output[0][6],3),' eV')
print('T2-S0=',np.round(output[0][7],3),' eV')
print('T3-S0=',np.round(output[0][8],3),' eV')
print('T4-S0=',np.round(output[0][9],3),' eV')
print('T5-S0=',np.round(output[0][10],3),' eV')
print('ISC=',np.round(output[0][3]-output[0][8],3),' eV')