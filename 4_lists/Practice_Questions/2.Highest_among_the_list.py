'''Find the hightest number among the list of the numbers'''

#Answer:

#taking the input from the user
num_list=input("Enter the numbers separated by space: ").split()
#converting the string to the integer
for n in range(0, len(num_list)):
    num_list[n]=int(num_list[n])

#finding the highest number
highest_num=0   #let the highest number be 0
for num in num_list:
    #check if the number is greater than highest number
    if num>highest_num:
        #yes, then assign the number to the highest number
        highest_num=num

#printing the highest number
print(f'Highest number among the list is {highest_num}')

#-----------------------------------------------------------------------------------------#
