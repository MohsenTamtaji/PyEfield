# PyEfield

A Python-based Machine Learning (ML) algorithm for the calculation of Efiled around gold-silica nanoparticlers.

************************************************************
Developed by Mohsen Tamtaji (mtamtaji@connect.ust.hk) under the supervision of Professor Zhengtang Tom Luo at HKUST, [Advanced Materials & Devices Laboratory](https://tomluogroup.wixsite.com/nanomaterials)


The developed ML algorithm can be used for the prediction of electric field around gild-silica nanoparticles. 

Deep neural networks (DNN) is trained based on FDTD-calculated data.

The ML model is also applicable for the calculation of HOMO-LUMO energy levels and Jablonski diagram of several photosensitizers(MB, TPP, and RB) in the presence of electric field. The data are from TD-DFT calculations using Gaussian 09. 

************************************************************

![SAC](si-auR63D.png)

************************************************************

# Requirments and Dependencies:

PyEfield needs the following pakages:

1-[pickle](https://scikit-learn.org/stable/install.html)

2- [matplotlib](https://matplotlib.org/stable/users/installing/index.html)

3- [numpy](https://numpy.org/install/)

************************************************************

# Running PyEfield:

Note: There is not "pip install" of this version yet, so you need to download the ML algorithm and run the program as follows:

1- Download the **TNNEfield2.pickle** files into your directory


2- Download the **PyEfield.py** and put into your directory, open in your PyCharm, Spider, or other Python environments, define the dimention and shape in the **PyEfield.py** file and run the code. The program will plot the electric filed for gold-silica core-shell nanoparticles.

3- Enjoy :)

In order to calculate the HOMO-LUMO energy levels and jablonski diagram for MB, RB, or TPP photosensitizers in the presence of E (eV):

1- Clone the MLTDDFT-Copy file

2- Open **PyTDDFT.py** in your PyCharm, Spider, or other Python environments, define **E** and the name of photosensitizer, and run the code. The program will print the HOMO, LUMO energies. It alos calculate T1, S1, and ISC energies. Please see the following picture:

![Jablonski](MLTDDFT - Copy/Jablonskidiagram.png)

Please note that **MB** stands for Methylene Blue, **RB**, stands for Rose Bengal, and **TPP** stands for Tetraphenylporphyrine. 

************************************************************

# Citation:

For the citation, please cite the following papers:

1- DOI: [10.1039/D1TA08337F](https://pubs.rsc.org/en/content/articlehtml/2022/ta/d1ta08337f)

2- https://doi.org/10.1021/acsanm.1c01436
