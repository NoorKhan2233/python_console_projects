import numpy as np
import time
def win_or_block_cell(arr,symbol):
    for row in range(3):
        if np.count_nonzero(arr[row,:] == symbol) == 2 and np.count_nonzero(arr[row,:] == ' ') == 1:
            return (row,np.where(arr[row,:] == ' ')[0][0])
        if np.count_nonzero(arr[:,row] == symbol) == 2 and np.count_nonzero(arr[:,row] == ' ') == 1:
            return (np.where(arr[:,row] == ' ')[0][0],row)
    if np.count_nonzero(np.diag(arr) == symbol) == 2 and np.count_nonzero(np.diag(arr) == ' ') == 1:
        empty_index = np.where(np.diag(arr) == ' ')[0][0]
        return (empty_index,empty_index)
    if np.count_nonzero(np.diag(np.fliplr(arr)) == symbol) == 2 and np.count_nonzero(np.diag(np.fliplr(arr)) == ' ') == 1:
        empty_index = np.where(np.diag(np.fliplr(arr)) == ' ')[0][0]
        return (empty_index,2-empty_index)
    return None

def winner(arr,symbol):
    return  np.any(np.all(arr == symbol,axis = 0)) or \
            np.any(np.all(arr == symbol, axis = 1)) or \
            np.all(np.diag(arr) == symbol) or \
            np.all(np.diag(np.fliplr(arr)) == symbol)
def is_draw(arr):
    return not np.any(arr == ' ')

def gpt_computer_move(arr,gpt_computer_symbol,my_computer_symbol):
        print('GPT Computer move:')
        time.sleep(1)
        win_cell = win_or_block_cell(arr,gpt_computer_symbol)
        
        if win_cell:
                arr[win_cell] = gpt_computer_symbol
                return
        block_cell = win_or_block_cell(arr,my_computer_symbol)
        if block_cell:
                arr[block_cell] = gpt_computer_symbol
                return
        empty_cells = np.argwhere(arr == ' ')
        if len(empty_cells) > 0:
                random_move = empty_cells[np.random.choice(len(empty_cells))]
                arr[random_move[0],random_move[1]] = gpt_computer_symbol
                return

def count(arr):  # check for the number of occupied cell
    count = 0
    for x in np.nditer(arr):
        if x != ' ':
            count += 1
    return count

def my_computer_adjusted_move(arr,my_computer_symbol): # this function is responsible for computer move if there is no block and win cell
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
                arr[chosen_index] = my_computer_symbol
                arr = arr.reshape(3, 3)
                return True
            else:
                probabilities[non_occupied_cells] = 1/(len(non_occupied_cells))
                probabilities[occupied_cells] = 0
                indices = np.where(arr == arr)[0]
                chosen_index = np.random.choice(indices, p=probabilities)
                arr[chosen_index] = my_computer_symbol
                arr = arr.reshape(3, 3)
                return True

def my_computer_move(arr, my_computer_symbol,gpt_computer_symbol): # responsible for the move of computer
    print('My computer move:')
    time.sleep(1)
    win_cell = win_or_block_cell(arr,my_computer_symbol)
    if win_cell:
        arr[win_cell] = my_computer_symbol
        return
    block_cell = win_or_block_cell(arr,gpt_computer_symbol)
    if block_cell:
        arr[block_cell] = my_computer_symbol
        return
    if my_computer_adjusted_move(arr,my_computer_symbol):
        return 

def print_board(arr):
        for row in arr:
                print(' | '.join(row))
                print('-'*9)

def play():
    arr = np.full((3,3),' ')
    choice = input('Which one you wanna go first (1 for my_computer 2 for gpt_computer):')
    if choice == '1':
        my_computer_symbol = 'X'
        gpt_computer_symbol = 'O'
    else:
        my_computer_symbol = 'O'
        gpt_computer_symbol = 'X'
    if choice == '1':
        current_turn = 'my_computer'
    else:
        current_turn = 'gpt_computer'
    while True:
        print_board(arr)
        if current_turn == 'my_computer':
            my_computer_move(arr,my_computer_symbol,gpt_computer_symbol)
            if winner(arr,my_computer_symbol):
                print_board(arr)
                print('My computer win!')
                return
            current_turn = 'gpt_computer'
        else:
            gpt_computer_move(arr,gpt_computer_symbol,my_computer_symbol)
            if winner(arr,gpt_computer_symbol):
                print_board(arr)
                print('Your computer lose!')
                return
            current_turn = 'my_computer'
        if is_draw(arr):
            print_board(arr)
            print("It's a draw!")
            return
play()
