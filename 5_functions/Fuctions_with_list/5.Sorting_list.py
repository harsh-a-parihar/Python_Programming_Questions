'''Sort the given list without using functions and then print sorted list'''

#Solution:

#1.Find minimum element in list
#2.Append it to new list
#3.Remove it from original list

#defining function minimum
def minimum(lst):
    #assuming first element of list as min
    min=lst[0]
    #iterating over list
    for elem in lst:
        #comparing with min
        if elem<min:
            min=elem
    #returning min
    return min

#defining function to append and remove minimum element
def sorted_list(lst):
    #creating new list to store sorted elements
    new_list=[]
    #iterating over list
    while len(lst)>0:
        #find minimum element
        min=minimum(lst)
        new_list.append(min)
        lst.remove(min)

    #returning sorted list
    return new_list

#taking input
List=input('Enter elements of list separated by space: ').split()
#converting to int
for i in range(len(List)):
    List[i]=int(List[i])
print('List: ',List)

#calling function and printing result
print('Sorted list: ', sorted_list(List))

#------------------------------------------------------------------------------------------#
