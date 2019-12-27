from scipy import stats
import numpy as np

# The number of a is odd
a = [4, 4, 6, 7, 10, 11, 12, 14, 15]
Q1 = np.percentile(a, 25, interpolation='midpoint')
Q3 = np.percentile(a, 75, interpolation='midpoint')

print('The wrong iqr:', Q3-Q1)
print('The wrong iqr from stats', stats.iqr(a))

# Instead we need use the following function
def iqr_(m):
    m = np.array(m)
    n = m.size//2
    m_ = np.partition(m.ravel(), n + 1)
    return np.median(m_[n + m.size%2:]) - np.median(m_[:n])
    
print('The correct IQR:', iqr_(a))
print('Thanks Daniel Stackoverflow for the function')
# Referece:
# https://stackoverflow.com/questions/51943661/is-scipy-stats-doing-wrong-calculation-for-iqr/59505135#59505135
# If the length of the dataset is even
# We can use stats.iqr 
    
