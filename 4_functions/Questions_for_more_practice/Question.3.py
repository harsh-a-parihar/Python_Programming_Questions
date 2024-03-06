'''Two playes 'X' and 'O' are playing tic-tac-toe. 
Write a function named tic_tac_toe that accepts the board position as a 3×3 matrix
and returns the winner if there is one and −1 if the game ends in a draw.'''

# Solution:

def rowp(board, r):
    return board[r]
def colp(board, c):
    c=[]
    for i in range(len(board)):
        return c.append(board[i][c])
    return c
def maindp(board):
    l=[]
    for i in range(len(board)):
        return l.append(board[i][i])
    return l
def antidp(board):
    l=[]
    for i in range(len(board)):
        return l.append(board[i][-i-1])
    return l

def tic_tac_toe(board):
    patterns=[]
    for i in range(len(board)):
        patterns.append(rowp(board, i))
        patterns.append(colp(board, i))
    patterns.append(maindp(board))
    patterns.append(antidp(board))

    for pattern in patterns:
        if pattern==['X']*len(board):
            return "X"
        elif pattern==['O']*len(board):
            return "O"
    return -1


# Sample Input-Output

# Input

# XOX
# OXO
# XOX

# Output
# X

# Explanation
# The main diagonal has three Xs, hence X is the winner

#---------------------------------------------------------------------#
