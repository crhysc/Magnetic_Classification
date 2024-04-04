import numpy as np

import sklearn
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, davies_bouldin_score

from clusteval import clusteval

if __name__ == '__main__':
    
    #dataset
    X = np.loadtxt('rhysdata/X_data.txt', dtype=str)
    X = X.astype(float)

    #removing nan values. if a row contains a nan value, the row is deleted.
    deleted_rows = []
    for iy, ix in np.ndindex(X.shape):
        if np.isnan(X[iy,ix]) == True:
            deleted_rows.append(iy)
    deleted_rows = np.unique(deleted_rows)
    X = np.delete(X, deleted_rows, 0)
    

    #tune n_clusters hyperparameter
    ce = clusteval(cluster='agglomerative', evaluate='silhouette')
    results = ce.fit(X)
    ce.plot()
    ce.scatter(X)
    cluster_labels = results['labx']
    #    **optimal number of clusters appears to be 4**
    
    #model fit
    clustering = KMeans(n_clusters=4, random_state=5, n_init='auto')
    clustering.fit(X)
    y_pred = clustering.predict(X)
    
    # Compute silhouette score
    silhouette = silhouette_score(X, y_pred)
    print("Silhouette Score:", silhouette)

    # Compute Davies-Bouldin index
    db_index = davies_bouldin_score(X, y_pred)
    print("Davies-Bouldin Index:", db_index)