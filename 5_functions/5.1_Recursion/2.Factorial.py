'''Write a recursive function to calculate the factorial of a number.'''

#Solution:

#defining function and passing parameter num
def fact(num):
    #factorial of 1 is 1
    if num==1:
        return 1
    else:
        #using function into function
        return num*fact(num-1)
    
#taking input from user
number=int(input('Enter the number you want factorial of: '))
#calling function and printing result
print(f'Factorial of {number} is ', fact(number))

#---------------------------------------------------------------------------------------#
