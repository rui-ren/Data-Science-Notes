## Feature clustering

### Learning how to use agglomerative clustering

* Agglomerative feature clustering
* PCA

`FeatureAgglomeration` object.
* `n_clusters` keyword argument is used to specify the new feature dimension of the data

```
from sklearn.cluster import FeatureAgglomeration
agg = FeatureAgglomeration(n_clusters=2)
new_data = agg.fit_transform(data)
# the code uses FeatureAgglomeration object to reduce feature dimensionality from 4 to 2, then use fit_transform function to fit the clustering model on the data
```
