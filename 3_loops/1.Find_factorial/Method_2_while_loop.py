'''Create a program to calculate the factorial of a number using a while loop.'''

#Answer:

#firstly, create a variable 'num' to store the number to find its factorial.
num=int(input("Enter a number to find its factorial: "))


#check if the input is a negative number or not.
if num<0:
    print("The factorial of negative number does not exist.")
else:
    #create a variable 'fact' to store the factorial of the number.
    fact=1
    #use while loop to calculate the factorial of the number.
    while num>0:
        fact*=num
        num-=1
    print(f"The factorial of {num} is {fact}")

#----------------------------------------------------------------------------------------#