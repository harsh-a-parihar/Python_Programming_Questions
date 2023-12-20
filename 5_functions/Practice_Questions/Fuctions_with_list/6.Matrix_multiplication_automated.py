'''Write a python program to multiply two matrices using functions.'''

#Solution:

#1.Initialize result matrix with 0
#2.Consider two matrices mat1 and mat2
#3.Find dot product of two lists of mat1 and mat2

#defining function to initialize matrix with 0
def result_mat(dim):
    #creating a empty list
    r_mat=[]
    #appending lists from 0 to dim to maintain order
    for i in range(dim):
        r_mat.append([])
    #appending rows(0)/columns(0) from 0 to dim to maintain order
    for i in range(dim):
        for j in range(dim):
            r_mat[i].append(0)
    #returning result matrix
    return r_mat

#defining function to count row
def row(m,r):
    #order of row is equal to length of matrix in sq.matrix
    dim=len(m)
    #to collect row
    lst=[]
    #iterate over matrix's column and make no change in row
    for k in range(dim):
        lst.append(m[r][k])
    #return result row list
    return lst

#defining function to count column
def column(m,c):
    #order of column is equal to length of matrix in sq.matix
    dim=len(m)
    #to collect column
    lst=[]
    #iterate over matix's row and make no change in column
    for k in range(dim):
        lst.append(m[k][c])
    #return result column list
    return lst

#defining function for dot product of ith row of mat1 and jth column of mat2
def dot_product(r,c):
    #order of column/row is equal to length of matrix in sq.matrix
    dim=len(r or c)
    #create variable to answer
    ans=0
    #iterate over the mat1 and mat2
    for i in range(dim):
        ans+=r[i]*c[i]
    #return result
    return ans

#defining function for final multiplication of mat1 and mat2
def mul_mat(mat1,mat2):
    #order of the matrices must be equal of sq.matrix
    dim=len(mat1)
    #create variable c to store result(result_mat)
    c=result_mat(dim)
    #iterate over matrices
    for i in range(dim):
        for j in range(dim):
            c[i][j]=dot_product(row(mat1,i),column(mat2,j))





























