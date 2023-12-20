'''Find whether a given number is Palindrome(reverse of the number = itself) or not.'''

#Answer:

#collecting the number from the user.
num=int(input("Enter a number: "))
abs_num=abs(num)

#convert abs_num to the string form.
str_num=str(abs_num)
#now, reverse the string_number using indexing.
rev_str_num=str_num[0:0:-1]
#now, reconvert the reversed number string in int form.
rev_int_num=int(rev_str_num)

#checking whether the num is neg- or not.
if (num<0):
    rev_int_num=rev_int_num - (2*rev_int_num)
#checking whether the number is palindrome or not.
if (rev_int_num==num):
    print("Palindrome.")
else:
    print("Not a Palindrome.")

#----------------------------------------------------------------------------------------#

