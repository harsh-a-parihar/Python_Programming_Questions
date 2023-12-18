'''Write a program that switches the values(generally integer(int)) stored in the variables a and b.'''

#Answer:

#this program takes two inputs.
#the first input is stored in a variable called a.
a=input("Enter the first number:")
#the second input is stored in a variable called b.
b=input("Enter the second number:")

#check if the inputs are numbers or not by using type() function.
if type(a)==int and type(b)==int:
    #creat variable c and store value of a in c.
    c=a
    #now a is empty variable. So store variable b in a.
    a=b
    #now b is empty varible. So store value of c variable in b.
    b=c
    #now values of a and b are switched, so print both.
    print("a: " + b)
    print("b: " + a)
else:
    print("The one/all inputs are not numbers.")

#----------------------------------------------------------------------------------------#
