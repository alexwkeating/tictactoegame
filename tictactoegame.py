#check git commit
def display_board(board):
    print('\n'*100)
    print(f" {board[1]} | {board[2]} | {board[3]} \n-----------\n {board[4]} | {board[5]} | {board[6]} \n-----------\n {board[7]} | {board[8]} | {board[9]} ")

def player_input():
    player1 = 'Empty'
    player2 = 'Empty'
    while player1.upper() != 'X' and player1.upper() != 'O':
        player1 = input("Player 1, please choose if you want to be X or O.")
    player1 = player1.upper()
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    return (player1, player2)

def place_marker(board, marker, position):
    board[position] = marker

def check_win(board, mark):
    winvalue = False
    if board[1:4] == [mark, mark, mark] or board[4:7] == [mark, mark, mark] or board[7:] == [mark, mark, mark]:
        winvalue = True
    elif (board[1] == board[4] == board[7] and mark == board[1]) or (board[2] == board[5] == board[8] and mark == board[2]) or (board[3] == board[6] == board[9] and mark == board[3]):
        winvalue = True
    elif (board[1] == board[5] == board[9] or board[3] == board[5] == board[7]) and mark == board[5]:
        winvalue = True
    return winvalue

import random

def choose_first():
    first_to_play = random.randint(1,2)
    if first_to_play == 1:
        return "Player 1 will start first!"
    else:
        return "Player 2 will start first!"

def space_check(board, position):
    free_space = True
    if board[position] == 'X' or board[position] == 'O':
        free_space = False
    return free_space

def full_board_check(board):
    board_full = True
    
    for space in board[1:]:
        if space != 'X' and space != 'O':
            board_full = False
    return board_full

def player_choice(board):
     
    while True:
        position = None
        while position not in range(1,10):
            position = input("Choose the next place you would like, using the numbers from 1-9.")
            if position in '123456789':
            	position = int(position)
            else:
            	position = 0

        if space_check(board, position) == True:
            return position
        else:
            print("Space has already been used")

def replay():
    play_again = ''
    while play_again.lower() != 'yes' and play_again.lower() != 'no':
        play_again = input('Do you want to play again, yes or no?')
    return play_again.lower() == 'yes'



print('Welcome to Tic Tac Toe!')

while True:
    # Setting the game up
    game_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    player1, player2 = player_input()
    a = choose_first()
    print(a)
    if a == 'Player 1 will start first!':
        first_turn = 1
        second_turn = 2
    else:
        first_turn = 2
        second_turn = 1
    game_on = True
    while game_on:
        
        if first_turn == 1:
            #Player 1 Turn
            choice1 = player_choice(game_board)
            place_marker(game_board, player1, choice1)
            display_board(game_board)
            
            if check_win(game_board, player1):
                print('Player 1 Wins!')
                game_on = False
                break
            if full_board_check(game_board):
                print("Board is full, the game is a tie")
                game_on = False
                break
        
            # Player2's turn.
            choice2 = player_choice(game_board)
            place_marker(game_board, player2, choice2)
            display_board(game_board)
            
            if check_win(game_board, player2):
                print('Player 2 Wins!')
                game_on = False
                break
            
        else:
            # Player2's turn.
            choice2 = player_choice(game_board)
            place_marker(game_board, player2, choice2)
            display_board(game_board)
            
            if check_win(game_board, player2):
                print('Player 2 Wins!')
                game_on = False
                break
            if full_board_check(game_board):
                print("Board is full, the game is a tie")
                game_on = False
                break 
            #Player 1 Turn
            choice1 = player_choice(game_board)
            place_marker(game_board, player1, choice1)
            display_board(game_board)
            
            if check_win(game_board, player1):
                print('Player 1 Wins!')
                game_on = False
                break           

    if not replay():
        break       

