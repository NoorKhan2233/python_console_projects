# (Challenge Project: Tic-Tac-Toe with Player Against the Computer) Modify your script from the previous player_vs_player project so that the computer makes the moves for one of the play- ers. Also, allow the player to specify whether he or she wants to go first or second.

import numpy as np
import time

def win_cell(arr, computer_symbol):
    # winning cell for row 0
    if np.count_nonzero(arr[0] == computer_symbol) == 2 and np.count_nonzero(arr[0] == ' ') == 1:
        winning_cell = np.where(arr[0] == ' ')
        arr[0, winning_cell] = computer_symbol
        return True
    # winning cell for row 1
    if np.count_nonzero(arr[1] == computer_symbol) == 2 and np.count_nonzero(arr[1] == ' ') == 1:
        winning_cell = np.where(arr[1] == ' ')
        arr[1, winning_cell] = computer_symbol
        return True
    # winning cell row 2
    if np.count_nonzero(arr[2] == computer_symbol) == 2 and np.count_nonzero(arr[2] == ' ') == 1:
        winning_cell = np.where(arr[2] == ' ')
        arr[2, winning_cell] = computer_symbol
        return True

    # winning cell for column 0
    if np.count_nonzero(arr[[0, 1, 2], 0] == computer_symbol) == 2 and np.count_nonzero(arr[[0, 1, 2], 0] == ' ') == 1:
        winning_cell = np.where(arr[[0, 1, 2], 0] == ' ')
        arr[winning_cell, 0] = computer_symbol
        return True

    # winning cell for column 1
    if np.count_nonzero(arr[[0, 1, 2], 1] == computer_symbol) == 2 and np.count_nonzero(arr[[0, 1, 2], 1] == ' ') == 1:
        winning_cell = np.where(arr[[0, 1, 2], 1] == ' ')
        arr[winning_cell, 1] = computer_symbol
        return True

    # winning cell for column 2
    if np.count_nonzero(arr[[0, 1, 2], 2] == computer_symbol) == 2 and np.count_nonzero(arr[[0, 1, 2], 2] == ' ') == 1:
        winning_cell = np.where(arr[[0, 1, 2], 2] == ' ')
        arr[winning_cell, 2] = computer_symbol
        return True

    # winning cell for main diagonal
    if np.count_nonzero(arr[[0, 1, 2], [0, 1, 2]] == computer_symbol) == 2 and np.count_nonzero(arr[[0, 1, 2], [0,1,2]] == ' ') == 1:
        winning_cell = np.where(arr[[0, 1, 2], [0, 1, 2]] == ' ')
        arr[winning_cell, winning_cell] = computer_symbol
        return True

    # winning cell for anti diagonal
    if np.count_nonzero(arr[[0, 1, 2], [2, 1, 0]] == computer_symbol) == 2 and np.count_nonzero(arr[[0, 1, 2], [2,1,0]] == ' ') == 1:
        winning_cell = np.where(np.diag(np.fliplr(arr)) == ' ')
        np.fliplr(arr)[winning_cell, winning_cell] = computer_symbol
        return True


def block_cell(arr, human_symbol, computer_symbol):
    # winning cell for row 0
    if np.count_nonzero(arr[0] == human_symbol) == 2 and np.count_nonzero(arr[0] == ' ') == 1:
        winning_cell = np.where(arr[0] == ' ')
        arr[0, winning_cell] = computer_symbol
        return True
    # winning cell for row 1
    if np.count_nonzero(arr[1] == human_symbol) == 2 and np.count_nonzero(arr[1] == ' ') == 1:
        winning_cell = np.where(arr[1] == ' ')
        arr[1, winning_cell] = computer_symbol
        return True
    # winning cell row 2
    if np.count_nonzero(arr[2] == human_symbol) == 2 and np.count_nonzero(arr[2] == ' ') == 1:
        winning_cell = np.where(arr[2] == ' ')
        arr[2, winning_cell] = computer_symbol
        return True

    # winning cell for column 0
    if np.count_nonzero(arr[[0, 1, 2], 0] == human_symbol) == 2 and np.count_nonzero(arr[[0, 1, 2], 0] == ' ') == 1:
        winning_cell = np.where(arr[[0, 1, 2], 0] == ' ')
        arr[winning_cell, 0] = computer_symbol
        return True

    # winning cell for column 1
    if np.count_nonzero(arr[[0, 1, 2], 1] == human_symbol) == 2 and np.count_nonzero(arr[[0, 1, 2], 1] == ' ') == 1:
        winning_cell = np.where(arr[[0, 1, 2], 1] == ' ')
        arr[winning_cell, 1] = computer_symbol
        return True

    # winning cell for column 2
    if np.count_nonzero(arr[[0, 1, 2], 2] == human_symbol) == 2 and np.count_nonzero(arr[[0, 1, 2], 2] == ' ') == 1:
        winning_cell = np.where(arr[[0, 1, 2], 2] == ' ')
        arr[winning_cell, 2] = computer_symbol
        return True

    # winning cell for main diagonal
    if np.count_nonzero(arr[[0, 1, 2], [0, 1, 2]] == human_symbol) == 2 and np.count_nonzero(arr[[0, 1, 2], [0,1,2]] == ' ') == 1:
        winning_cell = np.where(arr[[0, 1, 2], [0, 1, 2]] == ' ')
        arr[winning_cell, winning_cell] = computer_symbol
        return True

    # winning cell for anti diagonal
    if np.count_nonzero(arr[[0, 1, 2], [2, 1, 0]] == human_symbol) == 2 and np.count_nonzero(arr[[0, 1, 2], [2,1,0]] == ' ') == 1:
        winning_cell = np.where(np.diag(np.fliplr(arr)) == ' ')
        np.fliplr(arr)[winning_cell, winning_cell] = computer_symbol
        return True

def winner(arr, symbol):  # check for the winner of the game
    return (np.any(np.all(arr == symbol,axis = 0)) or 
            np.any(np.all(arr == symbol, axis = 1)) or 
            np.all(np.diag(arr) == symbol) or
            np.all(np.diag(np.fliplr(arr)) == symbol))


def draw(arr):  # check for the draw
    return not winner(arr, 'X') and not winner(arr, 'O') and np.all(arr != ' ')


def count(arr):  # check for the number of occupied cell
    count = 0
    for x in np.nditer(arr):
        if x != ' ':
            count += 1
    return count

def computer_adjusted_move(arr,computer_symbol): # this function is responsible for computer move if there is no block and win cell
        if count(arr) >= 0:
            arr = arr.ravel()
            probabilities = np.zeros(arr.shape)
            occupied_cells = np.where(arr != ' ')[0]
            non_occupied_cells = np.where(arr == ' ')[0]
            probabilities_non_occupied_cells = 1/(len(non_occupied_cells)*4)
            if arr[4] in arr[non_occupied_cells]:
                probabilities[non_occupied_cells] = probabilities_non_occupied_cells
                probabilities[4] = 1-(probabilities_non_occupied_cells *
                                    (len(non_occupied_cells)-1))
                probabilities[occupied_cells] = 0
                indices = np.where(arr == arr)[0]
                chosen_index = np.random.choice(indices, p = probabilities)
                arr[chosen_index] = computer_symbol
                arr = arr.reshape(3, 3)
                return True
            else:
                probabilities[non_occupied_cells] = 1/(len(non_occupied_cells))
                probabilities[occupied_cells] = 0
                indices = np.where(arr == arr)[0]
                chosen_index = np.random.choice(indices, p=probabilities)
                arr[chosen_index] = computer_symbol
                arr = arr.reshape(3, 3)
                return True

def computer_move(arr, computer_symbol,human_symbol): # responsible for the move of computer
    print('computer move:')
    time.sleep(1)
    if win_cell(arr, computer_symbol):
        return 
    if block_cell(arr,human_symbol, computer_symbol):
        return 
    if computer_adjusted_move(arr,computer_symbol):
        return 

def human_move(arr):  # this is for human which is play with computer 
        while True:
            try:
                entry = input('Your Move:')
                move = list(map(int, entry.split()))
                if arr[move[0], move[1]] == ' ':
                    arr[move[0], move[1]] = 'X'
                    return
                else:
                    print('Cell occupied! Enter non-occupied cell')
            except (ValueError, IndexError):
                print(
                    'Invalid indices! Enter valid row and column indices(0-2). i.e 0 0')

def print_board(arr):
    for row in arr:
        print(' | '.join(row))
        print('-'*9)

def tic_tac_toe(arr): # this function lets the computer and human play
    while True:
        wish = input('Do you want to move first or not! (y/n):')
        
        if wish.lower() == 'y':
            print_board(arr)
            while True:
                human_move(arr)
                print_board(arr)
                if winner(arr,'X'):
                    print('You win!')
                    return
                if draw(arr):
                    print('Game draw!')
                    return
                computer_move(arr,'O','X')
                print_board(arr)
                if winner(arr,'O'):
                    print('You lose!')
                    return
        
        if wish.lower() == 'n':
            while True:
                computer_move(arr,'O','X')
                print_board(arr)
                if winner(arr,'O'):
                    print('You lose!')
                    return
                if draw(arr):
                    print('Game draw!')
                    return
                human_move(arr)
                print_board(arr)
                if winner(arr,'X'):
                    print('You win!')
                    return 
        else:
            print('Please! Enter y or n one of them i.e y')
    
    
arr = np.full((3,3),' ')
tic_tac_toe(arr)
