'''p and q are called twin primes if both p and q are primes and |p-q|=2. 
Write a function named `twin_primes` that accepts two integers p and q as arguments. 
It should return True if the arguments are twin primes and False otherwise.'''

# Solution:

# frist check if p/q are prime
def check_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# now check twin_primes
def twin_primes(p, q):
    return abs(p-q)==2 and check_prime(p) and check_prime(q)

# call function
print(twin_primes(int(input('p:')), int(input('q:'))))

# test-case
#Input   expected output
5           #True
7

#-----------------------------------------------------------------------------------------------#
