
# reference:  python for machine learning

import pandas as pd
from PCA_sk import *

df_wine = pd.read_csv(
    'https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data',
    header = None)

from sklearn.model_selection import train_test_split
X, y = df_wine.iloc[:, 1:].values, df_wine.iloc[:, 0].values
X_train, X_test, y_train, y_test = train_test_split(X, 
                                                    y, 
                                                    test_size=0.3,
                                                    stratify=y,
                                                    random_state=0)

# standardize the features 
                                                            
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train_std = sc.fit_transform(X_train)
X_test_std = sc.transform(X_test)

import numpy as np
cov_mat = np.cov(X_train_std.T)  # calculate the covariance for case
eigen_vals, eigen_vecs = np.linalg.eig(cov_mat)
#print('\Eigenvalues \n%s' % eigen_vals)

tot = np.sum(eigen_vals)
# sort the value in the decrease order
var_exp = [(i / tot) for i in 
            sorted(eigen_vals, reverse=True)]
# return the cumsum to check the cummulative variance
cum_var_exp = np.cumsum(var_exp)

import matplotlib.pyplot as plt
plt.bar(range(1,14), var_exp, alpha=0.5, align='center',
        label='individual explained variance')
        
plt.step(range(1, 14), cum_var_exp, where='mid',
        label='cumulative explained variance')
plt.ylabel('Exlained variance ratio')
plt.xlabel('Principal component index')
plt.legend(loc='best')
plt.show()

# Feature transformation
eigen_pairs = [(np.abs(eigen_vals[i]), eigen_vecs[:, i])
                for i in range(len(eigen_vals))]

#print(eigen_pairs)
# according to the eigen_value to select the model
eigen_pairs.sort(key=lambda k: k[0], reverse=True)


# change (13, ) to (13, 1) and stack together
w = np.hstack((eigen_pairs[0][1][:, np.newaxis],
               eigen_pairs[1][1][:, np.newaxis]))

# create the 13 x 2 dimensional projection
print('Matrix W:\n', w) 

print(X_train_std[0].dot(w))
X_train_pca = X_train_std.dot(w)

# data visualization for the calculation

colors = ['r', 'b', 'g']
markers = ['s', 'x', 'o']
for num, c, m in zip(np.unique(y_train), colors, markers):
    plt.scatter(X_train_pca[y_train==num, 0],
                X_train_pca[y_train==num, 1],
                c=c, label=num, marker=m)

plt.xlabel('PC 1')
plt.ylabel('PC 2')
plt.legend(loc='lower left')
plt.show()

