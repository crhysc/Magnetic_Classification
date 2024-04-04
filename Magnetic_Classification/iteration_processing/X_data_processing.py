import numpy as np
import pandas as pd
import os
import json
import subprocess

import matplotlib.pyplot as plt

import sklearn
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import scale

import sklearn.metrics as sm
from sklearn import datasets
from sklearn.metrics import confusion_matrix, classification_report

from matminer.featurizers.conversions import StrToComposition
from matminer.featurizers.composition import ElementProperty, ElementFraction

from matminer.featurizers.base import MultipleFeaturizer


if __name__ == '__main__':
    with open('Magnetic_Classification/romerodata/curie/processed_curie.json') as f:
        processed_curie = json.load(f)

    feature_dict = {
        'formula':[],
        'property':[]
        }

    for key in processed_curie:
            feature_dict['formula'].append(processed_curie[key]["composition"])
            feature_dict['property'].append(processed_curie[key]["curie_temperature"])
    df = pd.DataFrame(feature_dict)
    print("\n FEATURE DATA FRAME")
    print(df.head())
    print("\n")


    df = StrToComposition().featurize_dataframe(df, "formula")
    print("\n STRING TO COMPOSITION")
    print(df.head())
    print(type(df["composition"].values[0]))
    print("\n")

    composition_featurizer = MultipleFeaturizer([ElementFraction()])
    composition_features = composition_featurizer.featurize_dataframe(df,"composition", ignore_errors=True)
    print("\n MULTIPLE FEATURIZER")
    print(composition_features.head())
    print("\n")

    X = composition_features.values[:,:]
    X = np.delete(X, [0, 2], axis=1)
    row_num = []
    for iy, ix in np.ndindex(X.shape):
        if X[iy,ix] == 'to':
            row_num.append(iy)
    X = np.delete(X, row_num, axis=0)
    print("\n X INPUT DATA")
    print(X[1])
    print(X.shape)
    np.savetxt('Magnetic_Classification/rhysdata/X_data.txt', X, fmt='%s')
    subprocess.run(['open', 'Magnetic_Classification/rhysdata/X_data.txt'])