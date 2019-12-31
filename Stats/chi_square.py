# chi-square -->
# -----------------
#        H       T
#  E     25     25
#  O     28     22

# here didnot use the probability 

# STEP 1: Test statistic for testing goodness of fit to a discrete probability

import numpy as np

def chi_square(a, expec):
    a = np.array(a)
    expec = np.array(expec)
    if expec.shape[0] > 1:
        expec = np.sum(a) * expec
    else:
        expec = np.ones((a.shape[0])) * expec * np.sum(a)
    mat = (a - expec)**2 / expec
    return np.sum(mat)
    
# coin
chi = chi_square([28, 22], [0.5])
# dic
# Chi value 
chi = chi_square([2, 4, 8, 9, 3, 10], [1/6])
# Chi value : 9.666
# ddof : 5 --> accept Null Hypothesis , there is no statistical between observe and expected
#print(chi)


a = [9, 15, 9, 8, 6, 13]
chi_value = chi_square(a, [1/6])
print ('dice experiment for the calculation' , chi_value)

a = [31,25, 21]
b = [0.344,0.405,0.251]

chi_value = chi_square(a, b)
print (chi_value)

# STEP 2: Two sample test for indepence analysis

# Ho : Baby gender and baby heart rate are independent
# H1:  Baby gender and baby heart rate are not independent

# ---------------------------------------
# ----------Heart Rate ------------------
#       Low    High     Row total
# Girl   11     7         18
# Boy    17     5         22
# Total  28     12       Total 40


#  probability of independent events is the product of the probabilities of each event --> calculate the expected number of E.

a = [11, 7]
b = [17, 5]

def chi_sqaure_ind(a):
    # change to matrix
    new = np.array(a)
    row_sum = np.sum(new, axis=1)
    col_sum = np.sum(new, axis=0)
    mat = row_sum.reshape(-1,1) * col_sum.reshape(1,-1) / np.sum(new)
    chi_value = (new - mat)**2 / mat
    return np.sum(chi_value)
    
chi_value = chi_sqaure_ind([a, b])
print('chi-square independent value', chi_value)

## Critical value for Chi-Square : 2.706

# 1.231 < 2.706  thus we will accept Null hypothesis 
# conclude that Baby gender and baby heart rate are independent


# Conclusion : Chi-square = sum(O-E)**2 / EOFError
# DOF : df = (I-1) X (J-1)

# Example calculation:

a = [35, 12, 5]
b = [6, 24, 18]
chi_value = chi_sqaure_ind([a,b])
print('College GPA and CEE:', chi_value)

# Chi-square: 31.75

# Conclusion --> we should reject null hypothesis Critical value = 9.21

# DOF : (2-1) * (3-1)
# Thus CEE and GPA are correlated --> 

# Example 2: Children psychologist 

a = [32, 29]
b = [55, 61]
c = [10, 13]
chi_square = chi_sqaure_ind([a,b,c])
print('Freedom to choose performs better:', chi_square)
    
    
# Example 3: Tasting competition
a = [12, 31, 27]
b = [15, 40, 21]
c = [10, 9, 7]
chi_square = chi_sqaure_ind([a,b,c])
print('Task competitions:', chi_square)

# Example 4: Parents left handed

a = [8, 10, 12]
b = [178, 21, 21]

chi_square = chi_sqaure_ind([a,b])
print('Left hand:', chi_square)



"""





















