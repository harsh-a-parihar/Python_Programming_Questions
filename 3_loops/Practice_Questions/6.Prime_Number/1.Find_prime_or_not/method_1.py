'''Find if the given number is prime or not using loop'''

#Answer(Simple):
#Using flag variable.

#Take input from user.
num=int(input("Enter a number: "))

#check if the number is more then 1, because prime number is always greater then 1.
if num>1:
    #create a flag variable and set it to True.
    is_prime=True
    #loop from 2 to the number(num).
    for i in range(2, num):
        #check if the number is divisible by any number between 2 and num.
        if num%i==0:
            #if number is divisible by any number between 2 and num, then set the flag variable to False.
            is_prime=False
            #break the loop.
            break
    #check if the flag variable is True and print the result.
    if is_prime:
        print(num, "is a prime number.")
    else:
        print(num, "is not a prime number.")
else:
    print("Enter number greater then 1.")


#----------------------------------------------------------------------------------------#
#little inefficient way.

