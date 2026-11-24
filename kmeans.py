from sklearn.cluster import KMeans
import numpy as np 

x = np.array([[1, 1] , [2,1], [4,3], [5,4]])

kmeans = KMeans( n_cluster = 2 , random_state = 1)
kmeans.fit(x)

print("Cluster Labels: ", kmeans.labels_)
print("Cluster centroids: ", kmeans.cluster_centers_)
