## Nearest Neighbors

* find the nearest neighbors for a data observation

### Finding the nearest neighbors

In `scikit-learn`, we implement the nearest neighbors approach with `NearestNeighbors`
return `default = 5`, we can set `n_neighbors=2` to change the return.

```
data = np.array([
  [5.1, 3.5, 1.4, 0.2],
  [4.9, 3. , 1.4, 0.2],
  [4.7, 3.2, 1.3, 0.2],
  [4.6, 3.1, 1.5, 0.2],
  [5. , 3.6, 1.4, 0.2],
  [5.4, 3.9, 1.7, 0.4],
  [4.6, 3.4, 1.4, 0.3],
  [5. , 3.4, 1.5, 0.2],
  [4.4, 2.9, 1.4, 0.2],
  [4.9, 3.1, 1.5, 0.1]])

from sklearn.neighbors import NearestNeighbors
nbrs = NearestNeighbors()
nbrs.fit(data)
new_obs = np.array([5., 3.5, 1.6, 0.3])
dists, knbrs = nbrs.kneighbors(new_obs)
```
Notice: the return `knbrs` is the indice of the nearest point.




