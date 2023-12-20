'''Create a python program to find the prime numbers in a given range using loops'''

#Answer(optimize method):

#import math library
import math

#take input range(start, end) from user
start=int(input("Enter the start of the range: "))
end=int(input("Enter the end of the range: "))

#print prime numbers in given range
print(f'Prime numbers between {start} and {end} are:')

#loop for each number in the given range
for num in range(start, end+1):
    #assume number is prime, until proven otherwise
    is_prime=True
    #check if number is greater than 1
    if num>1:
        #check divisibility from 2 to the square root of the number
        for i in range(2, int(math.sqrt(num))+1):
            if (num%i)==0:
                #if divisible then its not prime
                is_prime=False
                #break the loop
                break
        #check if number is prime
        if is_prime:
            #print the number
            print(num, end=', ')


#--------------------------------------------------------------------------------#
#More optimised method