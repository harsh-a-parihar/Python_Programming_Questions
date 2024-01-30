'''Number of times a character appears in the word.'''

#Solution:

word=input('Enter the word: ')
char=input('Enter char to find its frequecy: ')

#method.1
freq=0
for i in word:
    if i==char:
        freq+=1
print(f'{freq} times.')

#method.2
frequency=word.count(char)
print(f'{frequency} times.')

#---------------------------------------------------------------------#
