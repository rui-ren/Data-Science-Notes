from scipy import stats
import numpy as np
import warnings

# The number of a is odd
a = [4, 4, 6, 7, 10, 11, 12, 14, 15, 100]
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

def qt_(m):
    m = np.array(m)
    n = m.size//2
    m_ = np.partition(m.ravel(), n+1)
    q1 = np.median(m_[:n])
    q3 = np.median(m_[n + m.size%2:])
    return q1, q3

print('The correct IQR:', iqr_(a))
print('Thanks Daniel Stackoverflow for the function')
# Referece:
# https://stackoverflow.com/questions/51943661/is-scipy-stats-doing-wrong-calculation-for-iqr/59505135#59505135
# If the length of the dataset is even
# We can use stats.iqr 
   
# Denoise:   
# Key property of IQR is its resistance to the distorting effect of extreme scores
# IQR as the measure of variablity along with the median as the measure of central tendency

#  The usage of interquartile range -->
# 1. plot the box plot
# Lower limit = Q1 - 1.5*IQR
# Upper limit = Q3 + 1.5*IQR

# define the denoise function
def iqr_outlier_rm(dt_input):
    if len(dt_input) % 2 == 0:
        warnings.warn("Check if need to use another Q1")
    dt_input = np.array(dt_input)
    #Q1, Q3 = np.percentile(dt_input, [25, 75], interpolation='midpoint')
    IQR = iqr_(dt_input)  
    Q1, Q3 = qt_(dt_input)
    lower_l = Q1 - 1.5 * (IQR)
    upper_l = Q3 + 1.5 * (IQR)
    return dt_input[np.array(dt_input >= lower_l)& np.array(dt_input <= upper_l)]

print('the original data', a)
print('the data after denoise', iqr_outlier_rm(a))
