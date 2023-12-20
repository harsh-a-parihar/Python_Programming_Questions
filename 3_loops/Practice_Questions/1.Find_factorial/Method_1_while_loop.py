'''Create a proper program to calculate the factorial of a number(positive integer) using a while loop.'''

#Answer:

#first, collect a number to find its factorial and store in variable 'num'.
num=int(input("Enter a number to find its factorial: "))


#check if the input is a negative number or not.
if num<0:
    print("The factorial of negative number does not exist.")
else:
    #create a variable 'factorial' to store the factorial of the number.
    factorial=1
    #create a variable 'x' to store iteration(number of times the loop will run).
    x=1

    #create a while loop to calculate the factorial of the number.
    while x<=num:
        factorial=factorial*x
        #increment the value of x by 1.(Iteration)
        x=x+1
    print(f"The factorial of {num} is {factorial}")


#----------------------------------------------------------------------------------------#