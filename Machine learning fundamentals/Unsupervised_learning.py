# working with unlabeled data -- Clustering analysis

import numpy as np
import pandas as pd
import scipy as sp
import sklearn as sk

from sklearn.datasets import make_blobs

X, y = make_blobs(n_samples=150,   # how many sample we need use
                  n_features=2,    # n_features
                  centers=3,       # how many center point
                  cluster_std=0.5,
                  shuffle=True,
                  random_state=0
                  )
                  
import matplotlib.pyplot as plt
plt.scatter(X[:,0], X[:,1],
            c='white',
            marker='o',
            edgecolor='black',
            s=50)
                    
plt.grid()
plt.tight_layout()
plt.show()


from sklearn.cluster import KMeans

km = KMeans(n_clusters=3,  # input the k value
            init='random', # random selection for the first center
            n_init=10,     # run 10 times to random selection for first step
            max_iter=300,  # Stop condition 1: maximum iteration
            tol=1e-04,     # Stop condition 2: the minimum change of center
            random_state=0)

y_km = km.fit_predict(X)

plt.scatter(X[y_km == 0,0],
            X[y_km == 0,1],
            s=50,
            c='lightgreen',
            marker='s',
            edgecolor='black',
            label='Cluster 1'
            )
 
plt.scatter(X[y_km == 1,0],
            X[y_km == 1,1],
            s=50,
            c='orange',
            marker='o',
            edgecolor='black',
            label='Cluster 2'
            )
            
plt.scatter(X[y_km == 2,0],
            X[y_km == 2,1],
            s=50,
            marker='v',
            c='purple',
            edgecolor='black',
            label='Cluster 3'
            )
plt.scatter(km.cluster_centers_[:,0],
            km.cluster_centers_[:,1],
            s=250,
            marker='*',
            c='red',
            edgecolor='black',
            label='Centroids'
            )
            
plt.legend(scatterpoints=1)
plt.grid()
plt.tight_layout()
plt.show() 
            
