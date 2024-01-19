'''Find the factorial of the given number(user_input) using recursion.'''

#Solution:

#create recursive function to find factorial of any 'num'
def factorial(num):
    #check if num is less than 1
    if num<0:
        return 'Not-defined!!'
    else:
        #check if num is 1/0, then it's fact is 1
        if (num==1) or (num==0):
            return 1
        #otherwise, recall function with parameter 'num-1' and * to 'num'
        else:
            return num*factorial(num-1)

#take input from user
number=int(input('Enter number to find its factorial: '))

#call the function and print result
ans=factorial(number)
print(f'factorial of {number} is {ans}')

#-----------------------------------------------------------------------------------------------#
