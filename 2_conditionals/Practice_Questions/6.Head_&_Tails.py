'''You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".'''

#Answer:

#import random module
import random

#generate random number between 0 and 1 and store it in a variable.
random_num=random.randint(0,1)

#if random number is 0 then print Heads else print Tails.
if random_num==0:
    print("Heads")
else:
    print("Trails")

#----------------------------------------------------------------------------------------#

