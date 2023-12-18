'''Create a program that counts the number of digits in an integer using for loop.'''

#Answer:

#firstly, we need to take input from user
num=abs(int(input("Enter a number: ")))
#convert num into string form.
str_num=str(num)

#now, we need to initialize a variable to count the number of digits
count=0
#count the number of letters in the string using for loop and print the result.
for c in str_num:
    count+=1
print(f'There are {count}, in the given {num}')

#----------------------------------------------------------------------------------------#
