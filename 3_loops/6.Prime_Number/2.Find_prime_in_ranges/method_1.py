'''Create a python program to find the prime numbers in a given range using loops'''

#Answer(simple method)):


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
        #check if number is divisible by any number between 2 and number itself
        for i in range(2, num):
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
#Not optimised method