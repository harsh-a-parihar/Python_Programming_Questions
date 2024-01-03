'''Write a program that automatically prints the solution to the FizzBuzz game. These are the rules of the FizzBuzz game.'''

#Answer:

#Rules:
#Your program should print each number from 1 to 100 in turn and include number 100.
#case.1-When the number is divisible by 3 then instead of printing the number it should print "Fizz".
#case.2-When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
#case.3-And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

#create variable 'number' and assign number(100) till you want FizzBuzz game.
number=100

#start loop 1 to 100
for num in range(1,100+1):
    #check for case.3(if divisible by both 3 and 5 or not) first
    if (num%3==0) and (num%5==0):
        print('FizzBuzz')
    #check for case.1(if divisible by 3 or not)
    elif (num%3==0):
        print('Fizz')
    #check for case.2(if divisible by 5 or not)
    elif (num%5==0):
        print('Buzz')
    #otherwise, just print the number itself
    else:
        print(num)

#-----------------------------------------------------------------------------------------------------------------------#