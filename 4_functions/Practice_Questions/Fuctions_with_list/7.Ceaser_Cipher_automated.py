'''Write a python program to automate famous ceaser cipher encryption in which we encode(shift of alphabets) and decode(reshift of alphabets) 
any message(words,sentence,etc.)'''

#Answer:

#Method.1

#create a list of all the alphabets in english
alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m',
             'n','o','p','q','r','s','t','u','v','w','x','y','z']

#create a function to encrypt the message
def encrypt(simple_message,shift):
    encoded_message=''
    for a in simple_message:
        #check if the 'char' is in 'alphabets' list, if yes find shifted_letter and add to encoded_text otherwise add 'char' itself 
        if a in alphabets:
            shifted_letter=(alphabets[(alphabets.index(a)+shift)%26])    #%26 is bcz, list has only range(0,26)
            encoded_message+=shifted_letter
        else:
            encoded_message+=a
    print(f"The encryted message is '{encoded_message}'")

#create a function to decrypt the message
def decrypt(encrypted_message,shift):
    decoded_message=''
    for a in encrypted_message:
        #check if the 'char' is in 'alphabets' list, if yes find shifted_letter and add to encoded_text otherwise add 'char' itself
        if a in alphabets:
            reshifted_letter=(alphabets[(alphabets.index(a)-shift)%26])    #%26 is bcz, list has only range(0,26)
            decoded_message+=reshifted_letter
        else:
            decoded_message+=a
    print(f"The decrypted message is '{decoded_message}'")

#create a loop asking user if he wants to continue or stop
should_continue=True
while should_continue:
    #take inputs(encode/decode,message,shift) from the user
    coding=input("Type 'encode' -> encrypt and 'decode' -> decrypt:\n")
    message=input('Enter your message:\n').lower()
    shift=int(input('Number of shifts:\n'))

    #check the user's coding(encode/decode) and print result accordingly
    if coding=='encode':
        encrypt(simple_message=message,shift=shift)
    elif coding=='decode':
        decrypt(encrypted_message=message,shift=shift)

    #if user says 'no' to continue end the loop    
    user_choice=input("Want to continue? Type 'yes' or 'no'\n")
    if user_choice=='yes':
        continue
    elif user_choice=='no':
        should_continue=False
    else:
        print("Wrong choice!")
        break

#---------------------------------------------------------------------------------------------------------------#

#Method.2

#create a list of all the alphabets in english
alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m',
             'n','o','p','q','r','s','t','u','v','w','x','y','z']

#create a function 'ceaser' to perform both encryption and decryption
def ceaser(coding,message,shift):
    coded_text=''
    if coding=='decode':
        shift*=-1
    for l in message:
        position=alphabets.index(l)
        new_position=(position+shift)%26    #%26 is bcz, list has only range(0,26)
        coded_text+=alphabets[new_position]
    print(f"The {coding}d result is '{coded_text}'")

#create a loop asking user if he wants to continue or stop
should_continue=True
while should_continue:
    #take inputs(encode/decode,message,shift) from the user
    operation=input("Type 'encode' -> encrypt and 'decode' -> decrypt:\n")
    user_text=input('Enter your message:\n').lower()
    shift=int(input('Number of shifts:\n'))

    #call the 'ceaser' function
    ceaser(coding=operation,message=user_text,shift=shift)
    
    #if user says 'no' to continue end the loop    
    user_choice=input("Want to continue? Type 'yes' or 'no'\n")
    if user_choice=='yes':
        continue
    elif user_choice=='no':
        should_continue=False
    else:
        print("Wrong choice!")
        break
    
#---------------------------------------------------------------------------------------------------------------#
