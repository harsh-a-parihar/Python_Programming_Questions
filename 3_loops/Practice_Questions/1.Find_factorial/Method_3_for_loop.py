'''Create a program to calculate the factorial of a number using for loop.'''

#Answer:

#firstly, create a variable 'num' to store the number to find its factorial.
num=int(input("Enter a number to find its factorial: "))


#check if the input is a negative number or not.
if num<0:
    print("The factorial of negative number does not exist.")
else:
    factorial=1
    for i in range(num, 1, -1):
        factorial=factorial*i
    print(f"The factorial of {num} is {factorial}")

#----------------------------------------------------------------------------------------#
