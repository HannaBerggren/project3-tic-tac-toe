from time import sleep  # welcome title animation
import time  # game statement to disappear after a few seconds
import sys  # to access functions and variables
import random  # for computer moves


# welcome title with animation

welcome_title = "Welcome to play Tic Tac Toe game!\n"

for x in welcome_title:
    print(x, end='')
    sys.stdout.flush()
    sleep(.1)


# main variables for the gameboard, player's move, winners name and scores
# to access them inside the functions using the global statement

player_move = 'X'
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
winner = None
name = None
x_score = 0
o_score = 0


# instructions for the user to play the game

show_instructions = '''

Here are the instructions to play: \n
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
    Asks the user to enter 'P' in order to play the game
    '''
    while True:
        start_game_input = input("Type 'P' to play the game:\n").lower()
        if start_game_input == 'p':
            # making game starting statement disappear after a few seconds
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


# checking possible winning options
# accessing winner variable within the function

def check_rows(board):
    '''
    Checks possible horizontal winning options
    '''
    global winner
    if board[1] == board[2] == board[3] and board[1] != ' ':
        winner = board[1]
        return True
    elif board[4] == board[5] == board[6] and board[4] != ' ':
        winner = board[4]
        return True
    elif board[7] == board[8] == board[9] and board[9] != ' ':
        winner = board[7]
        return True


def check_column(board):
    '''
    Checks possible vertical winning options
    '''
    global winner
    if board[1] == board[4] == board[7] and board[1] != ' ':
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[8] != ' ':
        winner = board[2]
        return True
    elif board[3] == board[6] == board[9] and board[9] != ' ':
        winner = board[3]
        return True


def check_diagonal(board):
    '''
    Checks possible diagonal winning options
    '''
    global winner
    if board[1] == board[5] == board[9] and board[9] != ' ':
        winner = board[1]
        return True
    elif board[3] == board[5] == board[7] and board[7] != ' ':
        winner = board[3]
        return True


def check_tie(board):
    '''
    Checks for a draw, prints a message saying "It's a Tie".
    '''
    if board.count(' ') > 1:
        return False
    else:
        return True


# changing player from player 'X' to computer 'O'

def change_player():
    '''
    changing player from 'X' to 'O'
    '''
    global player_move
    if player_move == 'X':
        player_move = 'O'

    else:
        player_move = 'X'


def computer_move(board):
    '''
    Chooses a random computer move after the player's choice
    '''
    while player_move == 'O':
        pc_move = random.randint(1, 9)
        if board[pc_move] == ' ':
            board[pc_move] = 'O'
            change_player()


def the_winner(board):
    '''
    Checks the winner or a tie,
    evaluating the possible winning options
    defined above
    '''
    if check_rows(board) or check_diagonal(board) or check_column(board):
        check_score()
        game_board(board)

        if winner == 'X':
            print("Yeyy, You won!\n")
        elif winner == 'O':
            print("Oops, the Computer won!\n")

        first_page()

    elif check_tie(board):
        game_board(board)
        print("It's a Tie!\n")
        first_page()
    else:
        return None


def check_score():
    '''
    Increases the score for whoever wins the game
    '''
    if winner == 'X':
        global x_score
        x_score += 1
    elif winner == 'O':
        global o_score
        o_score += 1
    else:
        return None


# clear the board if user want to play again


def reset_board():
    '''
    Resets the board if user wants to play again
    '''
    board.clear()
    board.extend([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])


def first_page():
    '''
    When the game ends the user have a choice if they want
    to play again or quit
    '''
    print("*** Game Ended *** \n")

    print("Enter '1' to play again.")
    print('Enter "Q" if you want to quit the game.\n')
    while True:
        global name
        make_a_choice = input().strip()
        if make_a_choice.lower() == 'q':
            print(f'Thank you for playing the game {name}.')
            quit()
        elif make_a_choice == '1':
            print(f'Welcome again {name}')
            start_game()
            reset_board()
            user_choice()

        else:
            print("Invalid selection. Please select '1' or 'q'")


# the actual game

def user_choice():
    '''
    checks users choice on board
    '''
    while True:
        game_board(board)

        while True:

            try:

                user_input = int(input('Select a spot 1 to 9! :\n'))

                if user_input in range(1, 10):
                    if board[user_input] == ' ':
                        board[user_input] = player_move
                        break
                    else:
                        print(
                            f"The spot {user_input} is taken. "
                            "Choose another number.")
                else:
                    print('Invalid selection. Number must be between 1/9!\n')

            except ValueError:
                print("Oops! Invalid input. Please enter a valid number:\n")

        the_winner(board)
        check_tie(board)
        change_player()
        computer_move(board)
        the_winner(board)
        check_tie(board)


user_choice()