'''Find the first palindrom word from a sentence.'''

# Solution:

sent=input('sent: ')
lst=(sent).split(' ')

rev=''
flag=False

#loop through each word of list
for i in lst:
    #reverse the word
    rev=i[::-1]
    #check
    if i==rev:
        flag=True
        print('Palindrom word',i)
        break
if flag==False:
    print('no word here is palindrom word')

#----------------------------------------------------------------------------------------------#
