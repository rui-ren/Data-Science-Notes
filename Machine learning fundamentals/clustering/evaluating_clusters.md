
## Evaluating Clusters

* Evaluation metrics

when you don't have access to any true cluster assignments, the best we can do to evaluate clusters is to just take a look at them and see if they make sense with respect to the dataset and domain.

1. adjusted Rand index (ARI)

The regular rand index gives a measurement of **similarity** between the true clustering assignments and the predicted clustering assignments.

2. ARI value range [-1, 1], **Negative scores** represent bad labelings, **random labeling** will get a score near 0, and **perfect labelings** get a score of 1


```
from sklearn.metrics import adjusted_rand_score
true_labels = np.array([0, 0, 0, 1, 1, 1])
pred_labels = np.array([0, 0, 1, 1, 2, 2])

# the symmetric data
ari = adjusted_rand_score(true_labels, pred_labels)
print('{}\n'.format(ari))

# perfect labeling
perf_labels = np.array([0, 0, 0, 1, 1, 1])
ari = adjusted_rand_score(true_labels, perf_labels)
print('{}\n'.format(ari))

# permuted labeling
permuted_labels = np.array([1, 1, 1, 0, 0, 0])
ari = adjusted_rand_score(true_labels, renamed_labels)
print('{}\n'.format(ari))

true_labels2 = np.array([0, 1, 2, 0, 3, 4, 5, 1])

# bad labeling
pred_labels2 = np.array([1, 1, 0, 0, 2, 2, 2, 2])
ari = adjusted_rand_score(true_labels2, pred_labels2)
```

### Notice
1. `sklearn adjusted_rand_score` is symmetric
2. permutations in the labeling or changing the label names does not affect the score

## Adjusted mutual information (AMI)

```
from sklearn.metrics import adjusted_mutual_info_score
ami = adjusted_mutual_info_score(pred_labels, true_labels)
print('{}\n'.format(ami))

# perfect labeling
perf_labels = np.array([0, 0, 0, 1, 1, 1])
ami = adjusted_mutual_info_score(true_labels, perf_labels)
```