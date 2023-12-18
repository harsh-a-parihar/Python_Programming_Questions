'''Write a function called that takes a list of numbers as the input and returns the minimum and maximum value in the list.'''

#Solution:

#defining function
def min_max(lst):
    #assuming first element of list as min and max
    min=lst[0]
    max=lst[0]
    #iterating over list
    for elem in lst:
        #comparing with min
        if elem<min:
            min=elem
        #comparing with max
        if elem>max:
            max=elem
    #returning min and max
    return min,max

#taking input
List=input('Enter elements of list separated by space: ').split()
#converting to int
for i in range(len(List)):
    List[i]=int(List[i])
print('List: ',List)

#calling function and printing result
print('Minimum and Maximum in list: ',min_max(List))

#-----------------------------------------------------------------------------------#
