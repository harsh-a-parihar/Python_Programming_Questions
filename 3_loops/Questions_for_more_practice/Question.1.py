'''India features in a cricket tournament in which it has to play 5 games. 
The runs scored by four players in each of the 5 games is given to you as input. 
Process this input and create a dictionary named total. The keys of this dictionary is the name of the player. 
The corresponding value is the sum of the runs scored by that player across the 5 games. 
The keys of the dictionary should be inserted in the order in which the players are processed from the input area. 
You can assume that all four players have played all five games. The input will contain exactly four lines. Print the dictionary.'''

# Solution:

D = dict()  # to store the players and total runs
for i in range(4):
    L = input().split(',')
    name = L[0]
    total_runs=0
    for j in L[1:]:
        runs=int(j)
        total_runs+=runs
    # add dictionary
    D[name]=total_runs

print(D)

#sample-input-output

# Input
# Virat,101,88,93,0,120
# Rohit,50,100,30,140,80
# Sky,10,20,30,40,50
# Shreyas,100,0,0,100,0

# Output
# {'Virat': 402, 'Rohit': 400, 'Sky': 150, 'Shreyas': 200}

#-------------------------------------------------------------------------------------------------#
