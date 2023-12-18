'''Write python program for a simple 3x3 Matrix addition.
Matix addition is the operation of adding two matrices by adding the corresponding entries together.'''

#Answer(Simple. Not using functions):

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

#adding elements of m1 and m2 and storing in result
for i in range(dimention):
    for j in range(dimention):
        result[i][j]=m1[i][j]+m2[i][j]

#printing result
print("Resultant matrix is: ", result)

#-------------------------------------------------------------------------------------#
