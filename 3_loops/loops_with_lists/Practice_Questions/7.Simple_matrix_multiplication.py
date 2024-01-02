'''Write a python program to multiply two matrices.
Matix multiplication is a very common operation in deep learning.'''

#Answer(Simple):


#dimention of matrix is 3x3
dimention=3

#creating two empty matrix m1 and m2
m1=[]
m2=[]

#taking elements in 3x3 order for matrix m1
s1=[10, 20, 30]
s2=[40, 50, 60]
s3=[70, 80, 90]

#taking elements in 3x3 order for matrix m2
t1=[11, 22, 33]
t2=[44, 55, 66]
t3=[77, 88, 99]

#appending elements in m1 and m2
m1.append(s1)
m1.append(s2)
m1.append(s3)

m2.append(t1)
m2.append(t2)
m2.append(t3)

#creating empty matrix of order 3x3 for result
result=[[0,0,0],[0,0,0],[0,0,0]]

#result[i][j] is the dot product of ith row of m1 and jth column of m2
for i in range(dimention):
    for j in range(dimention):
        #k is the common index that runs from 0 to 2 for both m1 and m2
        for k in range(dimention):
            result[i][j]+=m1[i][k]*m2[k][j]

#printing result
print("Resultant matrix is: ", result)

#---------------------------------------------------------------------------------------------#
