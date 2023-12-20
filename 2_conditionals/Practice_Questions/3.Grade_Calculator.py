'''Design a program that takes a student's score as input and calculates their grade based on a 
grading scale (e.g., A, B, C, D, or F).'''

#Answer:

#create a varible 'score' to store the student's Score.
score=int(input("Enter your score: "))


#use if-elif-else statement to calculate the grade.
if score<0 or score>100:
    print("Invalid Score.")
else:
    if score>=90:
        print("Your grade is A.")
    elif score>=80:
        print("Your grade is B.")
    elif score>=70:
        print("Your grade is C.")
    elif score>=60:
        print("Your grade is D.")
    elif score>=50:
        print("Your grade is E.")
    else:
        print("Your grade is F.")

#----------------------------------------------------------------------------------------#
