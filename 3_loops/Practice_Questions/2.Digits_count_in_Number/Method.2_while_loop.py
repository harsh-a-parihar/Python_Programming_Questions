'''Create a program that counts the number of digits in an integer using a while loop.'''

#Answer:

#firstly, we need to take input from user
num=abs(int(input("Enter a number: ")))

#now, we need to initialize a variable to count the number of digits
count=1

#now, we need to use while loop to count the number of digits
while num>9:
    num=num//10
    count+=1
print("Number of digits in the give number is ",count)

#----------------------------------------------------------------------------------------#
