'''Find the average of the elements in a list using functions.'''

#Solution:

#defining function
def average(List):
    sum=0
    #iterating over list
    for num in range(len(List)):
        sum+=List[num]
    avrage=sum/len(List)
    #returning average
    return avrage

#taking input
lst=input('Enter elements of list separated by space: ').split()
#converting to int
for i in range(len(lst)):
    lst[i]=int(lst[i])
print('List: ', lst, '\n')

#calling function and printing result
print('Average of list: ', (average(lst)))           #you can also round() the ans

#-----------------------------------------------------------------------------------#
