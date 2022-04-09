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

1- [pickle](https://scikit-learn.org/stable/install.html)

2- [matplotlib](https://matplotlib.org/stable/users/installing/index.html)

3- [numpy](https://numpy.org/install/)

4- [rdkit](https://www.rdkit.org/docs/Install.html)


************************************************************

# Running PyEfield:

Note: There is not "pip install" of this version yet, so you need to download the ML algorithm and run the program as follows:

1- Download the **TNNEfield2.pickle** files into your directory


2- Download the **PyEfield.py** and put into your directory, open in your PyCharm, Spider, or other Python environments, define the dimention and shape in the **PyEfield.py** file and run the code. The program will plot the electric filed for gold-silica core-shell nanoparticles.


3- Enjoy :)

*****************************************************
In order to calculate the HOMO-LUMO energy levels and jablonski diagram for MB, RB, or TPP photosensitizers in the presence of E (eV):

1- Clone the MLTDDFT file

2- Open **PyTDDFTMB.py** in your PyCharm, Spider, or other Python environments, define the location of your files and also **E** in Volt/Angstrom (V/Å). The range of **E** is in +- 0.271 V/Å.


The program will print the HOMO, LUMO energies. It alos calculates S1, S2, T1, T2, T3, T4, T5, and ISC energies. Please see the following picture:

![Jablonski](https://github.com/MohsenTamtaji/PyEfield/blob/380ec7bf353f8f6db75d95336091d06f9650a583/MLTDDFT/Jablonski1.png)



3- Enjoy :)

************************************************************

# Citation:

For the citation, please cite the following papers:

1- DOI: [10.1039/D1TA08337F](https://pubs.rsc.org/en/content/articlehtml/2022/ta/d1ta08337f)

2- https://doi.org/10.1021/acsanm.1c01436
