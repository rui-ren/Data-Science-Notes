
## K-Mean clustering
* Assumption: dataset consists of **spherical** clusters, with this assumption, the k-means algorithm will create clusters of data observations that **circular** around the centroids.
* goal is to learn about k-means clustering
* understand why mini-batch clustering is used for large datasets

### K-mean algorithm
K-means clustering algorithm will separate the data into K clusters(the number of cluster is chosen by the user)

Centroids represents the "centers" of each cluster. K-means clustering algorithm is an iterative process. Each iteration, the algorithm will assign each data observation to the cluster with the closest centroid to the observation. (using regular distance metric)

* Note: the initialization of k-means are either randomly initialized or (better) initialized using the K-mean++ algorithm.

* Iteration stops: when no more changes in cluster assignment for any data observation.

#### Scikit-learn API

```
from sklearn.cluster import KMeans
# using k-mean++ centroid initialization by default
kmeans = KMeans(n_cluster=3)
# predefined data
kmeans.fit(data)
# cluster assignments
new_obs = np.array([
    [5.1, 3.2, 1.7, 1.9],
    [6.9, 3.2, 5.3, 2.2]
])
# predict clusters
kmeans.predict(new_obs)
```

### Mini-batch clustering
When dealing with very large datasets, regular K-means clustering can be very slow. To reduce the computation time, we can perform mini-batch K-means clustering, which is just regular K-means clustering applied to randomly sampled subsets of the data (mini-batches) at a time.

#### MiniBatchKMeans API

```
from sklearn.cluster import MiniBatchKMeans
kmeans = MiniBatchKMeans(n_clusters=3, batch_size=10)
# predefined data
kmeans.fit(data)

# cluster assignments
print(kmean.labels_)

# centroids
print(kmeans.cluster_centers_)

# prediction
new_obs = np.array([
    [5.1, 3.2, 1.7, 1.9],
    [6.9, 3.2, 5.3, 2.2]])
print(kmeans.predict(new_obs))
```

### Define KMeans function pipeline

```
def kmeans_clustering(data, n_clusters, batch_size):
    if batch_size:
        MiniBatchKMeans(n_clusters = n_clusters, batch_size = batch_size)
    else:
        kmeans = KMeans(n_clusters = n_clusters)
    kmeans.fit(data)
    return kmeans
```

