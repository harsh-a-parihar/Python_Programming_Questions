'''A data entry operator has a faulty keyboard. The keys 0 and 1 are very unreliable.
Sometimes they work, sometimes they don't. While entering phone numbers into a database, 
the operator uses the letter 'l' as a replacement for 1 and 'o' as a replacement for 0 whenever 
these binary digits let him down. Both 'l' and 'o' are in lower case. 'l' is the first letter of 
the word 'land', and not capital 'i'.
Accept a ten-digit number as input. Find the number of places where the numbers 0 and 1 have been replaced by letters. 
If there are no such replacements, print the string No mistakes. If not, print the number of mistakes (replacements) 
and in the next line, print the correct phone number.'''

# Solution:

num = input()
num_o = num.count('o')
num_l = num.count('l')
mistakes = num_o + num_l
if mistakes == 0:
    print('No mistakes')
else:
    print(f'{mistakes} mistakes')
    # replace all 'o' and 'l' with 0 and 1
    num = num.replace('o', 0)
    num = num.replace('l', 1)
    print(num)

#-------------------------------------------------------------------------------------------#
