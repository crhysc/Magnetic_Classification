import numpy as np

import sklearn
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, davies_bouldin_score
from sklearn.model_selection import GridSearchCV

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
    param_grid = {'n_clusters': range(1, 11)}

    clustering = KMeans(random_state=5, n_init='auto')
    grid_search = GridSearchCV(estimator=clustering, param_grid=param_grid, cv=5, scoring='silhouette_score')
    grid_search.fit(X)

    best_estimator = grid_search.best_estimator_
    print(f"Best Parameters: {grid_search.best_params_}")
    best_estimator.fit(X)

    y_pred = best_estimator.labels_

    
    # Compute silhouette score & Davies-Bouldin index
    silhouette = silhouette_score(X, y_pred)
    print("Silhouette Score:", silhouette)

    db_index = davies_bouldin_score(X, y_pred)
    print("Davies-Bouldin Index:", db_index)
