
# t-test to compare two wheat
import numpy as np
from scipy import stats

# (signal(residual) / noise())

# : difference between two means  --> difference signal
# : variance  increase the number size of sample --> we will reduce the noise

a = [15.2, 15.3, 16. , 15.8, 15.6, 14.9, 15. , 15.4, 15.6, 15.7, 15.5, 15.2, 15.5, 15.1, 15.3, 15. ]
b = [15.9, 15.9, 15.2, 16.6, 15.2, 15.8, 15.8, 16.2, 15.6, 15.6, 15.8, 15.5, 15.5, 15.5, 14.9, 15.9]

a = np.array(a)
b = np.array(b)

def t_value(a, b):
    
    a_mean = np.mean(a)
    b_mean = np.mean(b)
    
    a_var = np.std(a)
    b_var = np.std(b)
    print (b_var)
    t_value = abs(a_mean - b_mean) / np.sqrt(a_var**2 / len(a) + b_var**2 / len(b))
    return t_value

t_value = t_value(a, b)
print('t_value is %.2f' % t_value)

t_test = stats.ttest_ind(a, b)
print(t_test)
print('t_test is %.3f' % t_test[1])
