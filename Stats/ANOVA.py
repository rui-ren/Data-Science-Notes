# ANOVA
import numpy as np

def anova(a):
    dof = len(a) - 1
    a = np.array(a).T    
    mean_In = a.mean(axis=0)
    # sum of square in group --> SSW
    SSW = np.sum((a - mean_In)**2)
    # sum of square total --> SST
    mean_out = np.mean(a)
    SST = np.sum((a - mean_out)**2)
    # sum of square between groups
    SSB = np.sum((mean_In - mean_out)**2) * 5
    
    SSB_ = SSB / dof
    dof_w = a.shape[0]*a.shape[1] - (dof + 1)
    SSW_ = SSW / dof_w
    F = SSB_/SSW_
    return F, (dof, dof_w)
    
    
a = [2,3,7,2,6]
b = [10,8,7,5,10]
c = [10,13,14,13,15]

# relative frenquency
# critical value 3.89

F, _ = anova([a,b,c])

print('F _ value for the analysis', F)