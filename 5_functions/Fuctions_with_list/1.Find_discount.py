'''Find the discount of the given price using function'''

#Solution:

#defining a function discount with parameter price and discount
def discount_price(price, disc):
    #calculating the discount
    discount=(price*(disc/100))
    #returning the discount
    return 'Discount is: ' + str(discount)         #you can also round() the ans

#taking input from the user
price=int(input('Enter the price: '))
disc=int(input('Enter the discount rate: '))
#calling the function and printing the result
print(discount_price(price, disc))     

#--------------------------------------------------------------------------------------------#