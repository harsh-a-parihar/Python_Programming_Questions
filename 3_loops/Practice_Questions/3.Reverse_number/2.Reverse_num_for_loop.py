'''How to reverse the order the digits are in using for loop?'''

#Answer:

#firstly, we need to take input from user.
num=int(input("Enter a number:"))
#we need to use abs() function to convert negative numbers into positive numbers.
abs_num=abs(num)
#convert into string form.
str_absnum=str(abs_num)

#make an empty string to store the reverse string.
reverse=''
for i in str_absnum:
    reverse=i+reverse

#now, check if the given num was neg- or pos+ and print the result accordingly.
if num>=0:
    print(reverse)
else:
    print('-' + reverse)

#----------------------------------------------------------------------------------------#
