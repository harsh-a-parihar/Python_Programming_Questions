'''Find the input number given by the user in the random list using recursion.'''

#Solution:

#import random library
import random

#create a recursive funtion that finds 'num' from a random generated list.
def find_num(lst):
    #check if the list is empty
    if len(lst)==0:
        return 'Not present!!'
    #check the first number of list
    if num==lst[0]:
        return 'Present!!'
    #otherwise, recall the function itself from second number to last of list
    else:
        return find_num(lst[1:len(lst)])

#create a list to store 100 random integers between 1 to 1000
rlst=[]
for i in range(500):
    rlst.append(random.randint(1,1000))

print(rlst)
#take input from the user
num=int(input('Enter a number to check: '))

#call the function and print result
ans=find_num(rlst)
print(ans)

#-----------------------------------------------------------------------------------------------#
