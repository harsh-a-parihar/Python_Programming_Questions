'''Write a program using function which calculates the number of Upper case letters, lower case letters,
total number of characters and number of words.'''

#Solution

#defining function for upper case letters
def upper_case(sent):
    #assum upper case letters are 0
    upper=0
    #iterate over string
    for letter in sent:
        if (letter.isupper()):
            upper+=1
    #return result for upper case letters
    return upper

#defining function for lower case letters
def lower_case(sent):
    #assum lower case letters are 0
    lower=0
    #iterate over string
    for letter in sent:
        if (letter.islower()):
            lower+=1
    #return result for lower case letters
    return lower

#defining function for counting characters
def characters(sent):
    #assum total characters are 0
    char_letter=0
    #iterate over string
    for c in sent:
        char_letter+=1
    #return result for total characters
    return char_letter

#defining function for counting words
def words(sent):
    #assum tatal words equal to 0
    t_words=1
    #iterate over string
    for w in sent:
        if (w==' '):
            t_words+=1
    #return result for total words
    return t_words

#taking input from user
string=input('Enter the sentence: ')

#calling all the functions and printing result
uletter=upper_case(string)
print('Number of upper case letters are',uletter)
lletter=lower_case(string)
print('Number of lower case letters are',lletter)
char_letter=characters(string)
print('Number of characters in string are',char_letter)
total_word=words(string)
print('Number of words in the string',total_word)

#-----------------------------------------------------------------------------------------------#
