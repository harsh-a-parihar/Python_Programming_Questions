'''Accept the date in MM/DD/YYYY format as input from the user and print the date in DD-MM-YY format, 
by retaining only the last two digits in a year, replacing the forward slash with a dash and swapping
 the order of month and date.'''

# Solution:

date=input('data:')
month, day, year = date.split('/')
print(day, month, year[2:], sep='-')

#---------------------------------------------------------------------------------------------------#
