'''Find(search) if the element is in the list or not'''

#Answer:

#import random
import random

#create a empty list to collect elements
l=[]        #you can also manually fill the list and then search for the element

#loop to collect elements
for i in range(100000):
    l.append(random.randint(1,100000))

#initialize a varible 0
n=0
#loop to find the element
while (n>-1):
    n=int(input("Press -1 to exit or Enter the number to search: "))

    #flag to check if the element is in the list or not
    flag=0
    #loop to check
    for element in range(len(l)):
        if l[element]==n:
            flag=1
            break
    if flag==1:
        print("Element is in the list")
    else:
        print("Element is not in the list")

#--------------------------------------------------------------------------------------------#
