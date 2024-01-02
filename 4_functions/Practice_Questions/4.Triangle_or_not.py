'''Write a program using functions which checks whether the input coordinates form a triangle or not.'''
############################if sum of two sides is greater than third side then it is a triangle#############################


#Solution.1:Using distance formula

#defining function for measuring distance between points
def distance(xi,yi,xj,yj):
    return ((((xj-xi) ** 2) + ((yj-yi) ** 2)) ** 0.5)

#defining function for checking triangle
def istriangle(max,di,dj):
    if ((di+dj)>max):
        print('\nTriangle')
    else:
        print('\nNot a triangle')


#taking input
x1=float(input('Enter x1: '))
y1=float(input('Enter y1: '))
x2=float(input('\nEnter x2: '))
y2=float(input('Enter y2: '))
x3=float(input('\nEnter x3: '))
y3=float(input('Enter y3: '))

#calling distance function for all sides
d1=distance(x1,y1,x2,y2)
print('\nDistance between points 1 and 2: ',d1)
d2=distance(x2,y2,x3,y3)
print('\nDistance between points 2 and 3: ',d2)
d3=distance(x3,y3,x1,y1)
print('\nDistance between points 3 and 1: ',d3)

#checking for maximum distance
if d1>d2:
    if d1>d3:
        istriangle(d1,d3,d2)
    else:
        istriangle(d3,d1,d2)
elif d2>d3:
    istriangle(d2,d1,d3)
else:
    istriangle(d3,d1,d2)


#----------------------------------------------------------------------------------------------#


#Solution.2:Using slope formula

import math

#defining function for measuring slope between points
def slope(xi,yi,xj,yj):
    if (xi==xj):
        return (math.inf)
    else:
        return ((yj-yi)/(xj-xi))



#taking input
x1=float(input('Enter x1: '))
y1=float(input('Enter y1: '))
x2=float(input('\nEnter x2: '))
y2=float(input('Enter y2: '))
x3=float(input('\nEnter x3: '))
y3=float(input('Enter y3: '))

#slope of lines between points
s1=slope(x1,y1,x2,y2)
print('\nSlope of line between points 1 and 2: ',s1)
s2=slope(x2,y2,x3,y3)
print('\nSlope of line between points 2 and 3: ',s2)
#we don't need 3rd slope necessarily. We can check for 2 slopes only

#checking equality of at least two slopes for triangle
if s1==s2:
    print('\nNot a triangle')
else:
    print('\nTriangle')

#----------------------------------------------------------------------------------------------#
