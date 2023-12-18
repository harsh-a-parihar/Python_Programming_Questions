"""Write a program using Indexing, that takes a input as lowercase exactly 6 letters string(Plaintext) and transforms it into
encoded(Ciphertext- each letter of a word is shifted by one/two/three letter alphabetcally.) form."""

#Answer:

#create variable 'alphabets' and store all the alphabets(serialwise) in the form of string.
alpha='abcdefghijklmnopqrstubwxyz'

#now, collect a 6 letter string input from the person and store in variable 'string'.
string=str(input("Type a 6 letter word in lowercase: "))

#create an empty string called 'conv_string' to store transformed Ciphertext.
conv_string=''

#now as wkt, input has only 6 letter word, so for indexing we'll take 0 to 5 of 'string'.
#initiat variable 'x' to 0 for starting index from 0th index until 5th index, by iterating 'i+1' at every step.
#then, create variable 'sht' and assign it 1/2/3 - i.e. how many letter's shift you want for each letter in 'string'.
x=0
sht=285       #1 letter shift

#in the below code, firstly, we checked index of letters(0 to 5) in the alpha.
#secondly, we added 1 shift(sht) to all the index of letters(0 to 5) in the alpha.
#third, we did modulo(%) division of 26 to all the index of letter(0 to 5) in the alpha to make it in the range.
#forth, we changed the index into letter in the alpha which is a shifted letter.
#finally, we appended shifted letters one by one to 'con_string' variable to make a Ciphertext.
conv_string=conv_string + (alpha[(((alpha.index(string[0]))+sht)%26)])
conv_string=conv_string + (alpha[(((alpha.index(string[0+1]))+sht)%26)])
conv_string=conv_string + (alpha[(((alpha.index(string[0+2]))+sht)%26)])
conv_string=conv_string + (alpha[(((alpha.index(string[0+3]))+sht)%26)])
conv_string=conv_string + (alpha[(((alpha.index(string[0+4]))+sht)%26)])
conv_string=conv_string + (alpha[(((alpha.index(string[0+5]))+sht)%26)])

#at last, you can print the transformed string into Ciphertext by printing 'con_string'.
print(conv_string)

#----------------------------------------------------------------------------------------#

