'''Find all prime numbers less than the entered number'''

#Answer:

#take input from user
num=int(input("Enter a number: "))

#check if number is greater than and equal to 2
if num>2:
    print(2, end=', ')
#loop for each number from 3 to num
for i in range(3, num):
    #create a flag variable
    prime=True
    #check divisibility of number from 2 to i
    for j in range(2, i):
        if i%j==0:
            #if divisible then its not prime
            prime=False
            #break the loop
            break
    #check if number is prime
    if prime:
        print(i, end=', ')
else:
    print("Enter a number greater than 2")


#--------------------------------------------------------------------------------#
