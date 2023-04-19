from time import sleep # welcome title animation
import time # game statement to disappear after a few seconds
import sys # to access functions and variables


# welcome title with animation

welcome_title = "Welcome to play Tic Tac Toe game!"

for x in welcome_title:
    print(x, end='')
    sys.stdout.flush()
    sleep(.1)


# main variables for the gameboard, player's move, winners name and scores
# to access them inside the functions using the global statement

player_move = 'x'
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
winner = None
name = None
x_score = 0
o_score = 0


# instructions for the user to play the game

show_instructions = '''

Here are the instructions to play: /n
- The game displays a 3x3 grid
- You will start first with the symbol 'X'
- The computer will be shown as the opposite symbol 'O'
- Place your symbol typing a number from 1-9 on an empty spot
- The first among the players who have 3 same symbols in a line,
  horizontally, vertically or diagonally WINS!
- If all the 9 spots are full and no one wins it's a tie!
'''
