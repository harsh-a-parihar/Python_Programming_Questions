'''Write a program that asks the user for a number n and prints the sum of the numbers 1 to n'''

#Answer:

#collecting input from user
n = int(input("Enter a number: "))

#initializing sum
sum = 0
#looping through the range
for i in range(1, n+1):
    sum += i
print(f'The sum of the numbers 1 to {n} is {sum}')

#----------------------------------------------------------------------------------------#
