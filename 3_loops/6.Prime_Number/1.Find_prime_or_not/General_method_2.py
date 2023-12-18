'''Find if the given number is prime or not using loop'''

#Answer(General and Optimized):

#Take input from user.
num=int(input("Enter a number: "))

#check if the number is greater than 1
if num>1:
    #Assum that the number is prime until proven otherwise and set the flag variable to True
    is_prime=True
    #check the divisibility of the number from 2 to the square root of the number.
    #because if a number is not a prime, it must have at least one divisor less than or equal to its square root.
    #so we only need to check divisors from 2 to the square root of the number.
    for i in range(2, int(num**0.5)+1):
        if num%i==0:
            #if divisible, the number is not prime
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
#More optimized and efficient way.