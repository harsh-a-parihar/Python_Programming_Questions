'''Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.'''

#Answer:

#create a variable 'weight' to store the user's weight.
weight=float(input("Enter your weight in Kg:"))
#create a variable 'height' to store the user's height.
height=int(input("Enter your height im m:"))

#calculate the BMI of the user.
BMI=weight/(height**2)

#check the BMI of the user by using if-elif-else statement.
if BMI<18.5:
    print(f'Your BMI is {BMI}, you are underweight.')
elif BMI<25:
    print(f'Your BMI is {BMI}, you have a normal weight.')
elif BMI<30:
    print(f'Your BMI is {BMI}, you are slightly overweight.')
elif BMI<35:
    print(f'Your BMI is {BMI}, you are obese.')
elif BMI>=35:
    print(f'Your BMI is {BMI}, you are cliincally obese.')

#----------------------------------------------------------------------------------------#
