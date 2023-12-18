'''Find the sum of the elements of the list using function.'''

#Solution:

#defining a function sum_list with parameter list
def sum_list(list):
    #initializing the sum to 0
    sum=0
    #iterating through the list
    for n in list:
        sum+=n
    #returning the sum
    return sum

#collect input from user
el_list=input('Enter the list elements separated by space: ').split()

#convert each element to int type
for i in range(len(el_list)):
    el_list[i]=int(el_list[i])
print('List: ', el_list)

#calling the function and printing the result
print('Sum of the list elements is: ', sum_list(el_list))

#------------------------------------------------------------------------------------------#
