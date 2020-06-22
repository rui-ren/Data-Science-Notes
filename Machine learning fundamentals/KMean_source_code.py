
## K - Mean self.code the hardway

# The overview of this code
#   1. random initialization the centroid
#   2. calculate the distance 
#   3. update the new centroid 

import random
random.seed(4)


class KMeans:    
    # class KMeans as the value of 
    def __init__(n_clusters=8):
        self.n_clusters = n_clusters
    
    # fit the data value for the calculation
    def fit(data, k = None):
        """
        Args: 
            data: pandas dataframe format
            n_clusters: Number of clusters, default = 8
        output:
            centoird coordinate
        """
        if not k: 
            k = self.n_clusters
        
        # shape of the data
        (n_row, n_col) = data.shape
        
        # random selection
        initial_cluster = random.selections(range(n_row), k = k)
        
        # 
        