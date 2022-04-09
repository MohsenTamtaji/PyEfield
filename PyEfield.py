import numpy as np
import pickle
import matplotlib.pyplot as plt

Location=r"E:\Second paper\Efield\FDTDsimulations"# Define the Location of your files
Shape=1 # Define the shape of nanoparticle 1 stands for nanopsphere and 2 stands for nanocube
r=[[7],[23]] #Define the diameter of gold nanospere in nm. For example 7 and 20 nm

for i in range(np.size(r)):
    r[i][0] = (r[i][0]-5)/20
TrainingNumber=np.size(r)
loaded_model = pickle.load(open(Location+"\PyEfield"+str(Shape)+".pickle", 'rb'))
output = loaded_model.predict(r)
meshcellsx,meshcellsxx=501,250
x,y,EE = np.zeros((meshcellsxx, meshcellsx)),np.zeros((meshcellsxx, meshcellsx)),np.zeros((meshcellsxx, meshcellsx))
for TrainingData in range(TrainingNumber):
    jj = 0
    for i in range(meshcellsxx):
        for j in range(meshcellsx):
            x[i][j] = (i  - (meshcellsxx-1)) / (meshcellsxx-1) *4 * (r[TrainingData][0]*20+5)
            y[i][j] = (j  - (meshcellsxx-1)) / (meshcellsxx-1) *4 * (r[TrainingData][0]*20+5)
            EE[i][j] = output[TrainingData][jj]
            jj += 1
    plt.figure()
    CS=plt.contourf(y, x, EE, 500, cmap='jet')
    CS=plt.contourf(y, -x, EE, 500, cmap='jet')
    plt.colorbar(CS)
    plt.xlabel('x (nm)')
    plt.ylabel('y (nm)')
    plt.text(0,0,'Au')
    plt.text(0, 0, 'Au', fontsize=14,fontweight='bold', color='white')
    plt.text(r[TrainingData][0]*23+5, 0, 'SiO$_2$', fontsize=14,fontweight='bold', color='white')
    plt.show
plt.show()
