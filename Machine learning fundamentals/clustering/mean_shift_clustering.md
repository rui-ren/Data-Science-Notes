
## Mean Shift Clustering

* use mean shift clustering to determine the **optimal** number of clusters
* The mean shift clustering algorithm is not very scalable due to computation time and still makes the assumption that clusters have a "blob"-like shape.

### mean shift clustering algorithm
* Like the K-means clustering algorithm, the mean shift algorithm is based on finding cluster centeroids.

```
from sklearn.cluster import MeanShift
mean_shift = MeanShift()
# predefined data
mean_shift.fit(data)

# cluster assignments
print('{}\n'.format(repr(mean_shift.labels_)))

# centeroids
print('{}\n'.format(repr(mean_shift.cluster_centers_)))

new_obs = np.array([
    [5.1, 3.2, 1.7, 1.9],
    [6.9, 3.2, 5.3, 2.2]
])

# predict clusters
print('{}\n'.format(repr(mean_shift.predict(new_obs))))

```