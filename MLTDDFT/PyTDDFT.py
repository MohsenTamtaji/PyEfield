from rdkit.Chem import AllChem, Draw, rdqueries,  Fragments
from rdkit import Chem
import numpy as np
import pickle
import matplotlib.pyplot as plt
import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

Photosensitizer=['MB'] #Define the name of your mol file. Please put the mol file beside PyTDDFT.py file
#MB, RB, or TPP #MB stands for Methylene Blue, RB, stands for Rose Bengal, and TPP stands for Tetraphenylporphyrin.
E=0.05 #Define the intensity of field in eV. The range is in 0 to 0.271 eV

#************* Please don't make any changes in the following codes ***********
Propertyoriginal = pickle.load(open('Property.pkl', 'rb'))
Property=np.zeros((1,6))
filename = 'PyTDDFT.sav' # The name of SVR model. Make sure that the PyTDDFT.sav file is beside PyTDDFT.py file
loaded_model = pickle.load(open(filename, 'rb')) #Loading SVR model
for i in range(np.size(Photosensitizer)):
    mol = Chem.MolFromMolFile(Photosensitizer[i]+ '.mol')
    Draw.MolToFile(mol, Photosensitizer[i]+'.png')  # Save the structure of your SAC
    q = rdqueries.AtomNumEqualsQueryAtom(6)  # C
    NC = len(mol.GetAtomsMatchingQuery(q))
    q = rdqueries.AtomNumEqualsQueryAtom(7)  # N
    NN = len(mol.GetAtomsMatchingQuery(q))
    q = rdqueries.AtomNumEqualsQueryAtom(8)  # O
    NO = len(mol.GetAtomsMatchingQuery(q))
    q = rdqueries.AtomNumEqualsQueryAtom(16)  # S
    NS = len(mol.GetAtomsMatchingQuery(q))
    Nbenzene = Fragments.fr_benzene(mol)
    Property[i][0] =E
    Property[i][1] = NC
    Property[i][2] = NN
    Property[i][3] = NO
    Property[i][4] = NS
    Property[i][5] = Nbenzene
for i in range(np.size(Property[0,:])): #Normalization of input data
    Property[:,i]=(Property[:,i]-np.min(Propertyoriginal[:,i]))/(np.max(Propertyoriginal[:,i])-np.min(Propertyoriginal[:,i]))
filename = 'PyTDDFT.sav'
loaded_model = pickle.load(open(filename, 'rb'))
output=loaded_model.predict(Property)
print(Photosensitizer[0])
print('E=',np.round(E,3),' eV')
print('HOMO=',np.round(output[0][0],3),' eV')
print('LUMO=',np.round(output[0][1],3),' eV')
print('S1-S0=',np.round(output[0][2],3),' eV')
print('T1-S0=',np.round(output[0][3],3),' eV')
print('ISC=S1-T1',np.round(output[0][2]-output[0][3],3),' eV')