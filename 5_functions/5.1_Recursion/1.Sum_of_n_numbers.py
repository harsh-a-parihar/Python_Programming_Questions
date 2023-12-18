'''Write a program to count sum of first n number using recursion.'''

#Solution:

#defining function and passing parameter num(number).
def sum(num):
    #using recursion to find sum of first n num
    if num==1:
        return 1
    else:
        #putting function into same function
        return num+sum(num-1)
    
#taking input from user
num=int(input('Enter a number: '))
#calling function and printing result
print(f'Sum of first {num} numbers is ', sum(num))

#----------------------------------------------------------------------------------------#
