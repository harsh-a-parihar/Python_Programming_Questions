'''How to reverse the order the digits are in using while loop?'''

#Answer:

#firstly, we need to take input from user.
num=int(input("Enter a number:"))
#we need to use abs() function to convert negative numbers into positive numbers.
abs_num=abs(num)

#now, we need to initialize a variable to store the reversed number.
reversed_num=0

#now, we need to use while loop to reverse the number.
while abs_num>0:
    #we need to use % operator to get the last digit of the number.
    last_num=abs_num%10
    #adding the last digit to reversed_num variable.
    reversed_num=(reversed_num*10)+last_num
    #we need to use // operator to remove the last digit of the number.
    abs_num=abs_num//10


#now, we need to check if the original input number was negative or positive and print the reversed number accordingly.
if num<0:
    print(f"Reversed number is {'-' + reversed_num}")      #instead of -reversed_num, you can use (reversed_num*2)-reversed_num
else:
    print(f"Reversed number is {reversed_num}")

#----------------------------------------------------------------------------------------#
