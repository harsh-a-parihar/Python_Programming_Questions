'''Accept a positive integer n as input and print a "number arrow" of size n.'''

# Solution:

pnum=int(input('Enter a positive int: '))

# Straight
for i in range(1,1+pnum):
    for j in range(1,1+i):
        if (j!=i):
            print(j,end=' ')
        else:
            print(j)

# Reversing
for i in range(pnum-1,0,-1):
    for j in range(1,1+i):
        if (j!=i):
            print(j,end=' ')
        else:
            print(j)

#----------------------------------------------------------------------------------#
