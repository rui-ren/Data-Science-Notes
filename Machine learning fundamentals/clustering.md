
## clustering

* clustering using unsupervised machine learning methods of extracting insights from unlabeled datasets.
* unsupervised machine learning are centered to find similarities / differences between data observations and making inferences based on those findings


### Usage for clustering
1. anomaly detection (detecting real vs fraudulent data) to make research
2. find similarities between data observations

## Cosine Similarity

* Chapter goals is to understand how the cosine similarity metric measures the similarity between data observations

### definition
Cosine similarity is used in mathematics as a similarity metric for real-valued vectors, the numeric data observation is vector of real numbers. 

### Value 
It is value is between -1 and 1. Cosine similarity values closer to 1 represent greater similarity between the observations, while values closer to -1 represent more divergence. A value of 0 means that the two data observations have no correlation (neither similar nor dissimilar)

### formula

$$\cos (u,v)=\frac{u}{||u||_2} .\frac{v}{||v||_2}$$

`scikit-learn`, cosine similarity is implemented via `cosine_similarity` function.

```
from sklearn.metrics.pairwise import cosine_similarity
data = np.array([[1.1, 0.3],
                 [2.1, 0.6],
                 [-1.1,-0.4],
                 [0., -3.2]])
cos_sims = cosine_similarity(data)                 
```
if the only calculate one pair-wise data, the result will be `(i, i)`, `i` is number of observation.

if pass through two datasets, the result will be `(i, j)`

### code for largest cosine similarity

```
import numpy as np
cos_sims = cosine_similarity(data)
# no returns for np.fill_diagonal
np.fill_diagnoal(cos_sims, 0)
similar_indexes = cos_sims.argmax(axis=1)
```
* 2020-1-10














