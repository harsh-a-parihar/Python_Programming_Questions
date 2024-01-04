#Note: Complete all other Questions(1 to end) to get more understanding, before coming on this game.

'''Code the Hangman game in python. In this game you try to guess a word chosen randomly from given list of words
in the certain number of chances. You guess the word letter-by-letter.'''

#Code:


#importing all files and modules needed
import random
import arts
import word_list

#printing 'hangman' logo from arts.py file
print(arts.logo)

#choosing random word to be guessed from 'words' of word_list.py file
chosen_word=random.choice(word_list.words)

#create list 'blanks' to collect guesses in place of blanks('_')
blanks=[]
#adding '_' in blanks, length of chosen_word times
for b in range(len(chosen_word)):
    blanks.append('_')

#creating a flag(game_over) and assinging 'False' initially
game_over=False
#create variable 'lives' that is total number of chances(6) to guess
lives=6

#loop all the game functions till game is over 
while not game_over:
    #take input of guessed letter from player, store in guess
    guess=input('Guess letter: ')

    #check if guess already in blanks and alert player
    if guess in blanks:
        print(f'You have already guessed {guess}\n')

    #check if the letter in chosen_word and guess are same, if yes, then replace '_' of blanks with that letter
    for p in range(len(chosen_word)):
        letter=chosen_word[p]
        if letter==guess:
            blanks[p]=letter
    
    #show the blanks by convering it from list to string
    print(f"Complete word: {''.join(blanks)}\n")

    #see, if guess is not in the chosen_word
    if guess not in chosen_word:
        #alert player of wrong guess
        print(f'You guessed wrong letter. You have {lives-1} chance.\n')

        #now, reduce lives(chances) by 1 every time wrong guess
        lives-=1
        #if no more chances are left and blanks not filled, end the game and alert player he lost.
        if lives==0:
            game_over=True
            print(f'Word was {chosen_word}.\nYou Lose!!')
    else:
        #alert player of correct guess
        print(f'You guessed correct letter. You have {lives} chance.\n')

    #if no more '_' in blanks list it means it is filled, then eng the game and alert player he won.
    if '_' not in blanks:
        game_over=True
        print(f'Word was {chosen_word}.\nYou Win!!')
    
    #show the hangman stages art from arts.py correspoding to the every chance(lives)
    print(arts.stages[lives])

#------------------------------------------------------------------------------------------------------------------#
