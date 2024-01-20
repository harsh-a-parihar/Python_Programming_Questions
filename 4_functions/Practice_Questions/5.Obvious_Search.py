'''Search element in the list.'''

#Solution:

#create function to search
def obvious_search(lst,num):
    #check if the num is lst
    for i in lst:
        if (num==i):
            return 'Present!'
    return 'Not present!'

#create random list of numbers till 1000
rlist=list(range(1000))

#take input from user
user_input=int(input('Enter a number to search: '))

#call the function and show result
ans=obvious_search(rlist,user_input)
print(ans)

#------------------------------------------------------------------------------------------------#
