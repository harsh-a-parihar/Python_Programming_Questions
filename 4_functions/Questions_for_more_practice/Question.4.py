'''A square matrix M is said to be 
diagonal: if the entries outside the main-diagonal are all zeros 
scalar: if it is a diagonal matrix, all of whose diagonal elements are equal 
identity: if it is a scalar matrix, all of whose diagonal elements are equal to 1 
Write a function named matrix_type that accepts a matrix M as argument and returns the type of matrix. 
It should be one of these strings: diagonal, scalar, identity, non-diagonal. 
The type you output should be the most appropriate one for the given matrix.'''

# Solution:

def matix_type(M):
    diag=[]
    for i in range(len(M)):
        diag.append(M[i][i])
        for j in range(len(M)):
            if (i!=j) and (M[i][j]!=0):
                return 'non-diagonal'
    
    if diag==[1]*len(M):
        return 'identity'
    if diag==[M[0]]*len(M):
        return 'scalar'

    return 'diagonal'

#-------------------------------------------------------------------------------------------------#
