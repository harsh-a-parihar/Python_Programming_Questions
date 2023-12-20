'''Find if the birthday paradox(at least 2 persons with the same birthdays) is true or not'''

#Answer:

#import random
import random

#collect input from the user how many people are there?
peoples=int(input("How many people are there?\nInput: "))

#create a empty list that collects the birthdays of 30 people
birthdays = []

#generate 30 random numbers between 1 and 365(days of the year)
for i in range(peoples):
    birthdays.append(random.randint(1,365))

#sort the list
birthdays.sort()
#print the list of birthdays
print("Birthdays: ", birthdays)
#check if there are 2 people with the same birthday
#assum that birthdays are not repeated
flag=False
for i in range(peoples-1):
    if birthdays[i] == birthdays[i+1]:
        #if yes, birthdays are repeated
        flag=True
        break

#display the result
if flag:
    print("Birthday paradox is true.", birthdays[i],"and", birthdays[i+1], "are repeated.")
else:
    print("Birthday paradox is false, no birthdays are repeated.")

#---------------------------------------------------------------------------------------------#
