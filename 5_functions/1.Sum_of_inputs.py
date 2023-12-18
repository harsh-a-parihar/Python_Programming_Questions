'''Write a python program using functions to find the sum of n numbers.'''

#Solution:

#defining a function sum() and passing a parameter n1 and n2
def sum(n1, n2):
    #adding n1 and n2
    sum = n1 + n2
    print("Sum of two numbers is: ", sum)

#taking input from the user
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))

#calling the function sum() and passing the parameters
sum(num1, num2)

#--------------------------------------------------------------------------------------#