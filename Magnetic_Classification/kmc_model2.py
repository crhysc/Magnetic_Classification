import numpy as np

import sklearn
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, davies_bouldin_score
from sklearn.model_selection import GridSearchCV

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
    

    #model fit
    ce = clusteval(cluster='agglomerative', evaluate='silhouette')

    results = ce.fit(X)

    ce.plot()

    ce.scatter(X)

    cluster_labels = results['labx']