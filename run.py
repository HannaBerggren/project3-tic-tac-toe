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

Here are the instructions to play:
- The game displays a 3x3 grid
- You will start first with the symbol 'X'
- The computer will be shown as the opposite symbol 'O'
- Place your symbol typing a number from 1-9 on an empty spot
- The first among the players who have 3 of the same symbols in a line,
  horizontally, vertically or diagonally Wins!
- If all the 9 spots are full and no one wins, it's a Tie!
'''


def player_name():
    '''
    Gets player's name accepting only alphabetical characters
    '''
    while True:
        global name
        name = input("\nPlease Enter your Name:\n").capitalize()

        if name.isalpha():
            print("\n")
            print(f"Hi {name}, Welcome to the Game!")
            print(show_instructions)

            break

        else:
            print("Oops! Invalid input. Only letters are accepted.")
            print("\nPlease try again:)")


player_name()


def start_game():
    '''
    asks the user to enter 'P' in order to play the game
    '''
    while True:
        start_game_input = input("Type 'P' to play the game:\n").lower()
        if start_game_input == 'p':              
            # making Game Starting statement disappear after a few seconds
            game_starting = 'Game Starting...'
            print(game_starting, end="\r")
            time.sleep(1)
            print(" " * len(game_starting), end="\r")
            time.sleep(1)
            break
        else:
            print(f"{start_game_input} Incorrect Input. Enter 'P' to start.")


start_game()


def game_board(board):
    '''
    Prints scores at the top and the game board
    '''
    print('\n')
    print(f'Your Score: {x_score:>5}    Computer Score:{o_score:>5}')
    print('\n')

    print(board[1], "| ", board[2], "| ", board[3], "| ",)
    print('-'*15)
    print(board[4], "| ", board[5], "| ", board[6], "| ",)
    print('-'*15)
    print(board[7], "| ", board[8], "| ", board[9], "| ",)
    print('\n')
