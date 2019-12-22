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
#plt.show()

from sklearn.cluster import KMeans

km = KMeans(n_clusters=3,  # input the k value
            init='random', # random selection for the initial centroids
            n_init=10,     # run 10 times to random selection for initial centroids
            max_iter=300,  # Stop condition 1: maximum iteration
            tol=1e-04,     # Stop condition 2: the minimum inertia to declare convergence
            random_state=0)

y_km = km.fit_predict(X)

# print label 1
plt.scatter(X[y_km == 0,0],
            X[y_km == 0,1],
            s=50,
            c='lightgreen',
            marker='s',
            edgecolor='black',
            label='Cluster 1'
            )

# print label 2
plt.scatter(X[y_km == 1,0],
            X[y_km == 1,1],
            s=50,
            c='orange',
            marker='o',
            edgecolor='black',
            label='Cluster 2'
            )

# print label 3
plt.scatter(X[y_km == 2,0],
            X[y_km == 2,1],
            s=50,
            marker='v',
            c='purple',
            edgecolor='black',
            label='Cluster 3'
            )

# print centroids
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
#plt.show() 

# the metric for model's inertial and plot a graph
# elbow plot

distortions = []
for i in range(1, 11):
    km = KMeans(n_clusters=i,
                init='random',
                n_init=10,
                max_iter=300,
                random_state=0,
                )
    km.fit(X)
    distortions.append(km.inertia_)

plt.plot(range(1, 11), distortions, marker='o')
plt.xlabel('Number of cluster')
plt.ylabel('Inertia')
plt.tight_layout()
#plt.show()


# Quantifying the quality of clustering via silhouette plots
import numpy as np
from matplotlib import cm
from sklearn.metrics import silhouette_samples

km = KMeans(n_clusters=3,
            init="k-means++",  # speed up convergence
            n_init=10,
            max_iter=300,
            tol=1e-04,
            random_state=0
            )
              
y_km = km.fit_predict(X)
cluster_labels = np.unique(y_km)
n_clusters = cluster_labels.shape[0]
silhouette_vals = silhouette_samples(X, y_km, metric='euclidean')
y_ax_lower, y_ax_upper = 0, 0
yticks = []

plt.figure()

for i, c in enumerate(cluster_labels):
    c_silhouette_vals = silhouette_vals[y_km == c]
    c_silhouette_vals.sort()
    y_ax_upper += len(c_silhouette_vals)
    color = cm.jet(float(i)/ n_clusters)
    plt.barh(range(y_ax_lower, y_ax_upper), 
                   c_silhouette_vals, 
                   height=1., 
                   edgecolor='none', 
                   color=color)
    yticks.append((y_ax_lower + y_ax_upper) / 2.)
    y_ax_lower += len(c_silhouette_vals)
    
silhouette_avg = np.mean(silhouette_vals)   # the mean of the silhouette coefficient
plt.axvline(silhouette_avg, color='red', linestyle='--')

plt.yticks(yticks, cluster_labels + 1)
plt.ylabel('Cluster')
plt.xlabel('Silhouette coefficient')

plt.tight_layout()
plt.show()    
    
    
    
            
