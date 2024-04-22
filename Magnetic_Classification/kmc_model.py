import numpy as np
import pandas as pd
import os
import json
import subprocess

import matplotlib.pyplot as plt

import sklearn
from sklearn.cluster import KMeans
from sklearn import metrics
from sklearn.metrics import silhouette_score, davies_bouldin_score
import sklearn.metrics as sm

from matminer.featurizers.conversions import StrToComposition
from matminer.featurizers.composition import ElementProperty, ElementFraction

from matminer.featurizers.base import MultipleFeaturizer

from yellowbrick.cluster import KElbowVisualizer
from clusteval import clusteval




class data:
    def prepare(path):

        #opening file
        with open(path) as f:
            processed_curie = json.load(f)

        #creating feature dictionary
        feature_dict = {
            'formula':[],
            'property':[]
            }
        for key in processed_curie:
                feature_dict['formula'].append(processed_curie[key]["composition"])
                feature_dict['property'].append(processed_curie[key]["curie_temperature"])
        df = pd.DataFrame(feature_dict)

        #featurizing data
        df = StrToComposition().featurize_dataframe(df, "formula")
        composition_featurizer = MultipleFeaturizer([ElementFraction()])
        composition_features = composition_featurizer.featurize_dataframe(df,"composition", ignore_errors=True)

        #removing 'to' value in dataset
        df = composition_features.values[:,:]
        df = np.delete(df, [0, 2], axis=1)
        row_num = []
        for iy, ix in np.ndindex(df.shape):
            if df[iy,ix] == 'to':
                row_num.append(iy)
        df = np.delete(df, row_num, axis=0)
    
        #removing nan values
        df = df.astype(float)
        deleted_rows = []
        for iy, ix in np.ndindex(df.shape):
            if np.isnan(df[iy,ix]) == True:
                deleted_rows.append(iy)
        deleted_rows = np.unique(deleted_rows)
        df = np.delete(df, deleted_rows, 0)        

        np.savetxt('/Users/rhyscampbell/Documents/projects/Magnetic_Classification/rhysdata/dataframe.txt', df, fmt='%s')
        subprocess.run(['open', '/Users/rhyscampbell/Documents/projects/Magnetic_Classification/rhysdata/dataframe.txt'])

        return df

class n_clusters_tune:
    def elbow_method(X):
        km = KMeans(random_state=42, n_init='auto')
        visualizer = KElbowVisualizer(km, k=(2,10))
        return visualizer.fit(X), visualizer.show()
    def silhouette_eval(X):
        ce = clusteval(cluster='agglomerative', evaluate='silhouette')
        results = ce.fit(X)

class evaluate_with_metrics:
    def sil(df, clustering_labels):
        silhouette = silhouette_score(X, y_pred)
        print("Silhouette Score:", silhouette)

    def DB(df, clustering_labels):
        db_index = davies_bouldin_score(X, y_pred)
        print("Davies-Bouldin Index:", db_index)

    def CH(df, clustering_labels):
        ch_index = metrics.calinski_harabasz_score(X, y_pred)
        print("Calinski-Harabasz Index:", ch_index)
    
    def all_metrics(df, clustering_labels):
        silhouette = silhouette_score(X, y_pred)
        print("Silhouette Score:", silhouette)
        print('\n')
        db_index = davies_bouldin_score(X, y_pred)
        print("Davies-Bouldin Index:", db_index)
        print('\n')
        ch_index = metrics.calinski_harabasz_score(X, y_pred)
        print("Calinski-Harabasz Index:", ch_index)
        print('\n')

class clustering:
    def assign_labels(df):
        kmeans = KMeans(n_clusters=4, random_state=5, n_init='auto')  
        clustering_labels = kmeans.fit_predict(df)
        return clustering_labels

class visalization:
    def data_histogram(path):
        with open(path) as f:
            processed_curie = json.load(f)

        #creating the data array
        
        temp_list = []
        
        for key in processed_curie:
                temp_list.append(processed_curie[key]["curie_temperature"])
        array = np.array(temp_list)
        return array

if __name__ == '__main__':
     
    #import data
    file_path = '/Users/rhyscampbell/Documents/projects/Magnetic_Classification/romerodata/curie/processed_curie.json'
    
    #histogram
    array = visalization.data_histogram(file_path)
    print(array)