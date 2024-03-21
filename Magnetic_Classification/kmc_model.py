import numpy as np
import pandas as pd
import os

import matplotlib.pyplot as plt

import sklearn
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import scale

import sklearn.metrics as sm
from sklearn import datasets
from sklearn.metrics import confusion_matrix, classification_report

#datasets
chem_path = 'Magnetic_Classification/rhysdata/chemical_comps.txt'
temp_path = 'Magnetic_Classification/rhysdata/curie_temps.txt'

X = scale(np.loadtxt(temp_path))
Y = np.genfromtxt(chem_path, dtype=str)

#initializing clustering model
clustering = KMeans(n_clusters=3, random_state=5, n_init='auto')
clustering.fit(X)