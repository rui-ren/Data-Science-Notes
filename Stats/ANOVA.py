# one way ANOVA
import numpy as np
import itertools

def anova(a):
    # Degree of freedom
    dof = len(a) - 1
    num_total = len(list(itertools.chain.from_iterable(a)))
    dof_w = num_total - len(a)

    num_in_group = np.array([len(i) for i in a]).reshape(1,-1)
    length = len(set(map(lambda x: len(x), a))) == 1
    
    if not length:
        a = [np.array(i) for i in a]
        
    else:
        a = np.array(a).T
        
        # square of sum --> within
        SSB = np.array
    print(a)
    
    mean_In = [sum(i) for i in a]/num_in_group
    
    print(mean_In, '////////')
    # sum of square in group --> SSW
    SSW = sum(map(lambda x: x - mean_In, a)**2)
    
     
    # sum of square total --> SST
    mean_out = np.sum(a)/ num_total
    SST = sum(map(lambda x: x - mean_out, a)**2)
    
    # sum of square between groups
    SSB = np.sum(SST - SSW)
   
    # variance between groups 
    variance_between = SSB / dof
        
    # variance within groups df_error = N - C
    
    
    variance_within = SSW / dof_w
    
    # F score variance between group / variance within groups
    
    F = variance_between / variance_within
    return F, (dof, dof_w)
    
# relative frenquency
# critical value 3.89



if __name__ == "__main__":

    """
    a = [2,3,7,2,6]
    b = [10,8,7,5,10]
    c = [10,13,14,13,15]
    F, _ = anova([a,b,c])
    print('F _ value for the analysis', F)

    a = [82,93,61,74,69,70,53]
    b = [71,62,85,94,78,66,71]
    c = [64,73,87,91,56,78,87]
    F, _ = anova([a,b,c])
    print('F_ value for the student analysis', F)


    a = [1,2,5]
    b = [2,4,2]
    c = [2,3,4]
    F, dof = anova([a,b,c])
    print('F_ value for the student analysis', F, dof)
    """  
    # energy consumption in US
    
    NE = [15, 10, 13, 14, 13]
    MW = [17, 12, 18, 13, 15, 12]
    S = [11, 7, 9, 13]
    W = [10, 12, 8, 7, 9]
    F, dof = anova([NE,MW,S,W])
    print('F_ value for the student analysis', F, dof)
