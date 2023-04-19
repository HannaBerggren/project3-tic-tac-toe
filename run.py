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
