
## DBSCAN

* DBSCAN clusters data by finding dense regions in the dataset.
* High density regions
* Low density regions

### Assumptions:
* DBSCAN algorithm treats high-density regions as clusters in the dataset, and low-density regions are treats as noise and not placed in a cluster.
* Highly scalable
* makes no assumptions about the underlying shape of clusters in the dataset, can find arbitarily shaped clusters
* robust to noise
* no need to assume number of clusters.

### Neighbors and core samples --> Two parameters
* specify the maximum distance, `epsolo`, radius
* specify the minimum number of points

### Notion of points
1. core point (if the data points within the neighbors > minimum data points)
2. border point (reachable from the core points)
3. outlier point (not core point and cannot reachable)

### Attributes
1. directly density-reachable
2. density-reachable
3. density-connected

### Drawback

* DBSCAN is sensitive to the setting of parameters


```
from sklearn.cluster import DBSCAN
dbscan = DBSCAN(eps=1.2, min_samples=30)
# predefine data
dbscan.fit(data)

# cluster assignments
print('{}\n'.format(repr(dbscan.core_sample_indices_)))
num_core_samples = len(dbscan.core_sample_indices)
print('Num core samples: {}\n'.format(num_core_samples))

```


