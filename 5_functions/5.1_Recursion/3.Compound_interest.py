'''Write a program to calculate compound interest(interest rate 10%) using recursive function.'''

#Solution:

#defining function and passing parameters
def comp_interest(p,n,r=10):
    #if no. years is 1
    if n==1:
        return p*(1.1)
    else:
        return (comp_interest(p,n-1,r))*1.1
    
    
#taking inputs from user
p_amount=int(input('Enter principle amount: '))
n_years=int(input('Enter period of years: '))
#calling function and printing result
print(f'Compound Interest: ', comp_interest(p_amount,n_years))

#-----------------------------------------------------------------------------------------------#
