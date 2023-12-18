'''Find the length of the longest word from the set of words entered by the user.'''

#Answer:

#take input from user
words=input("Enter the words: ")

#initialise the length of longest word to 0
longest_word_len=0

#start loop for each word in the input
while (words!='0'):
    #count the length of the word
    count=0
    for i in words:
        count+=1
    #check if the length of the word is greater than the length of the longest word
    if count>longest_word_len:
        #if yes, update the length of the longest word
        longest_word_len=count
    #take input from user
    words=input("Enter the words: ")

#print the length of the longest word
print('The length of the longest word is %s.' %longest_word_len)

#--------------------------------------------------------------------------------#
