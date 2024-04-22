import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import metrics
from sklearn.metrics import silhouette_score, davies_bouldin_score
from yellowbrick.cluster import KElbowVisualizer
from clusteval import clusteval

class hyperparameter_tune:
    def elbow_method(X):
        km = KMeans(random_state=42, n_init='auto')
        visualizer = KElbowVisualizer(km, k=(2,10))
        return visualizer.fit(X), visualizer.show()
    def silhouette_eval(X):
        ce = clusteval(cluster='agglomerative', evaluate='silhouette')
        results = ce.fit(X)


class evaluate:
    def sil(X, y_pred):
        silhouette = silhouette_score(X, y_pred)
        print("Silhouette Score:", silhouette)

    def DB(X, y_pred):
        db_index = davies_bouldin_score(X, y_pred)
        print("Davies-Bouldin Index:", db_index)

    def CH(X, y_pred):
        ch_index = metrics.calinski_harabasz_score(X, y_pred)
        print("Calinski-Harabasz Index:", ch_index)
    
    def all_metrics(X, y_pred):
        silhouette = silhouette_score(X, y_pred)
        print("Silhouette Score:", silhouette)
        print('\n')
        db_index = davies_bouldin_score(X, y_pred)
        print("Davies-Bouldin Index:", db_index)
        print('\n')
        ch_index = metrics.calinski_harabasz_score(X, y_pred)
        print("Calinski-Harabasz Index:", ch_index)
        print('\n')

    def table(X, y_pred):
        
        data = [silhouette_score(X, y_pred), davies_bouldin_score(X, y_pred), metrics.calinski_harabasz_score(X, y_pred)]
        columns = ('Silhouette Score', 'Davies-Bouldin Index', 'Calinski-Harabasz Index')
        rows = ['Row {}'.format(row) for row in range(1, 3)]

        fig, ax = plt.subplots()
        ax.axis('tight')
        ax.axis('off')
        table = ax.table(cellText=data, colLabels=columns, rowLabels=rows, loc='center')

        plt.show()

if __name__ == '__main__':
    
    #dataset
    data = np.loadtxt('rhysdata/X_data.txt', dtype=str)
    data = data.astype(float)
    X = data_clean.remove_nan(data)
    


    #clustering
    kmeans = KMeans(n_clusters=4, random_state=5, n_init='auto')
    kmeans.fit(X)
    y_pred = kmeans.predict(X)
    clustering_labels = kmeans.fit_predict(X)
    
    

    evaluate.all_metrics(X, y_pred)
    print("\n")
    evaluate.all_metrics(X, clustering_labels)



