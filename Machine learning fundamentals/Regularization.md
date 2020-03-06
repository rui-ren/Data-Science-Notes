
## Regularization

In `data preprocessing` procedure, feature selection is the an important method to differentiate the relevant feature and irrelevant feature.

    - Solve high dimension problem. (feature selection and dimension reduction)
    - Reduce model complexity and easier learning
    
 Decision tree involves  `subset search` and `subset evaluation`, it can be a method of feature selection.

There are 3 feature selection methods:

### 1. Filter
Filter method is to first selection the feature, then train the machine learning model. With the method, feature selection and model training are `separated`.

### 2. Wrapper
Select the subset based on the performance of algorithm on the subset.

### 3. Embedding method

* L1
L1 can get the sparsity solution, and the $ \w$ weight can be zero. 

* L2
L2 regularization, the weight will approach 0, cannot be zero

L1 is easier to get the sparsity solution.

