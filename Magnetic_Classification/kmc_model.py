import numpy as np
import pandas as pd
import os
import json

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
    print(df.head())
    df = StrToComposition().featurize_dataframe(df, "formula")
    print(df.head())
    print(type(df["composition"].values[0]))

    #ep_feat = ElementFraction.from_preset(preset_name="pymatgen")
    #df = ep_feat.featurize_dataframe(df, col_id="composition")  # input the "composition" column to the featurizer
    #print(df.head())

# MultipleFeaturizer([ElementFraction(),ElementProperty.from_preset(preset_name="magpie")])

    composition_featurizer = MultipleFeaturizer([ElementFraction()])
    composition_features = composition_featurizer.featurize_dataframe(df,"composition", ignore_errors=True)
    print(composition_features.head())

# feature_names = composition_features.columns()[3:]

    X = composition_features.values[:,[1,3]]
    print(X)
    print(X.shape)