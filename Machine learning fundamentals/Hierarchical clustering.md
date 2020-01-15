
## Hierarchical Clustering

* learning hierarchical clustering via the agglomerative approach

### K-means vs. hierarchical clustering
* Hierarchical clustering allows us to cluster any type of data, since it doesn't make any assumptions about the data or clusters

### Agglomerative clustering

```
from sklearn.cluster import AgglomerativeClustering
agg = AgglomerativeClustering(n_clusters=3)
agg.fit(data)
print('{}\n'.format(repr(agg.labels_)))
```
 * since there's no centroids assumption, there's no `cluster_centers_`attributes.
 * there is also no `predict` function for making cluster predictions