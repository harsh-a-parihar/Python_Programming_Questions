'''Write a program that works out whether if a given number is an odd or even number.'''

#Answer:

#first, collect a number to find it is odd or even and store in variable 'num'.
num=int(input("Enter a number to check if, it is ODD or EVEN: "))

#wkt, to find even or odd number, we often check its divisibility by 2.
#if the number is divisible by 2 = EVEN, otherwise it is ODD.
#use conditional statements: 'if-else' or 'if-elif-else' to do this.

#firstly, check if the input is a number or not by using type() function.

if num%2==0:
    print("The number is EVEN.")
else:
    print("The number is ODD.")

#----------------------------------------------------------------------------------------#
