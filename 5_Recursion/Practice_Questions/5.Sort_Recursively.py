'''Sort the random generated list recursivly.'''

#Solution:

#import random library
import random as ran

#create a function to find minimum most value in list
def minimum(lst):
    min=lst[0]
    for i in lst:
        if i<min:
            min=i
    return min

#create recursive function to sort the unsorted list
def sort_list(lst):
    #if list is empty
    if (len(lst)==0 or len(lst)==1):
        return lst
    #find minimum value in random list and remove it
    mini=minimum(rlst)
    rlst.remove(mini)
    #recursively sort the smaller list
    return [mini] + sort_list(lst)

#create a random generated list of 50 numbers between 1 to 100
rlst=[]
for i in range(50):
    rlst.append(ran.randint(1,100))
print(f'Unsorted random list:\n{rlst}')

#call sort_list function and print sorted list
ans=sort_list(rlst)
print(f'Sorted list:\n{ans}')

#-----------------------------------------------------------------------------------------------#
