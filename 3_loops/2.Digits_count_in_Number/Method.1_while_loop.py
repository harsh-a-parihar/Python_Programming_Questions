'''Create a program that counts the number of digits in an integer using a while loop.'''

#Answer:

#firstly, we need to take input from user
num=abs(int(input("Enter a number: ")))

#now, we need to initialize a variable to count the number of digits
count=0

#now, we need to use while loop to count the number of digits
while num>0:
    count+=1
    num=num//10
print("Number of digits in the given number is: ",count)


#----------------------------------------------------------------------------------------#
