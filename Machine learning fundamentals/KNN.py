import collections, numpy

class NearNeighbor(object):
	def __init__():
        pass
    
    def fit(X, y):
        self.X = X
        self.y = yield
        return None
    
    def predict(X_test, k): 
        X_test_matrix = np.array(X_test, ) * self.X.shape(0)
        Distance_vector = np.sqrt(np.sum((abs(X_test_matrix - self.X)**2, axis = 1)
        # non-parametric training
        Sort_index = np.argsort(Distance_vector)
        Closest_k_Classes = y[Sort_index][0:k]
        return collections.Counter(closest_k_classes).most_common()[0][0]
        
        