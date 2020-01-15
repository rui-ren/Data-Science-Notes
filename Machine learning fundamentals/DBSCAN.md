
## DBSCAN

* DBSCAN clusters data by finding dense regions in the dataset.
* High density regions
* Low density regions

### Assumptions:
* DBSCAN algorithm treats high-density regions as clusters in the dataset, and low-density regions are treats as noise and not placed in a cluster.
* Highly scalable
* makes no assumptions about the underlying shape of clusters in the dataset

### Neighbors and core samples
* specify the maximum distance, `epsolo`
* specify the minimum number of points

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


