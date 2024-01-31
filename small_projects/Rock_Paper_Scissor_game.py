'''Rock-Paper-Scissor Game.'''

# Code:

import random as ran

def get_choices():
    options=['rock','paper','scissor']
    p_choice=input('Enter your choice(rock,paper,scissor): ')
    c_choice=ran.choice(options)
    choices={'player':p_choice, 'computer':c_choice}
    return choices

def check_result(player,computer):
    print(f'You chose {player}\nComputer chose {computer}\n')

    if player==computer:
        return "It's a tie."
    elif player=='rock':
        if computer=='scissor':
            return "You Win!"
        else:
            return "You Lose!"
    elif player=='paper':
        if computer=='rock':
            return "You Win!"
        else:
            return "You Lose!"
    elif player=='scissor':
        if computer=='paper':
            return "You Win!"
        else:
            return "You Lose!"

all_choices=get_choices()
result=check_result(all_choices['player'],all_choices['computer'])
print(result)


#Algorithm:
#take choices from player and computer
    #options:(r,p,s)
    #choice of player as input
    #choice of computer as random.choice(options)
    #keep choices in dic of player and computer and return on time.
#check winner between (player and computer)-->parameters
    #print boths choices
    #first look if its tie, and then check all possibilities
#lastly,call and save choices
#pass choices and parameter in check winner and print the result

#------------------------------------------------------------------------------------------------------#
