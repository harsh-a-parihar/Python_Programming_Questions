'''Find whether a given number is Palindrome(reverse of the number = itself) or not.'''

#Answer:

#collecting the number from the user.
num=int(input("Enter a number: "))
abs_num=abs(num)

#initializing the variable to store the reverse of the number.
rev=0

#using while loop to reverse the number.
while abs_num>0:
    #getting the last digit of the number.
    last_d=abs_num%10
    #adding the last digit to the reverse variable.
    rev=(rev*10)+last_d
    #removing the last digit from the number.
    abs_num=abs_num//10

#checking whether the num is neg- or not.
if (num<0):
    rev=rev-(2*rev)
#checking whether the number is palindrome or not.
if rev==num:
    print("Palindrome.")
else:
    print("Not a Palindrome.")

#----------------------------------------------------------------------------------------#
