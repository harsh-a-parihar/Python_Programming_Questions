'''Binary search.'''

#Solution:

#create a function to search
def binary_search(lst,num):

    #first element in the list
    start=0
    #last element in the list
    end=len(lst)-1

    #use while loop to look at the list and keep halving it
    while(end-start>1):

        #find the middle most element
        mid_element=(start+end)//2

        #if the mid element is equal to 'num' then return True and stop the code
        if (lst[mid_element]==num):
            return 'Present!!'

        #if the mid element is more than 'num' cut the right side and retain the left side
        if (lst[mid_element]>num):
            end=mid_element-1
        
        #if the mid element is less than 'num' cut the left side and retain the right side
        if (lst[mid_element]<num):
            start=mid_element+1

    #if it is equal to 1, then there is exactly two elements
    if (lst[start]==num) or (lst[end]==num):
        return 'Present!!'
    else:
        return 'Not present!!'

#create a sorted list of range 1000
sorted_lst=list(range(1000))
#take the input from the user to search in the list
user_input=int(input('Enter the number(range:1000) to search: '))

#call the function and print result
result=binary_search(sorted_lst,user_input)
print(result)

#-----------------------------------------------------------------------------------------------#
