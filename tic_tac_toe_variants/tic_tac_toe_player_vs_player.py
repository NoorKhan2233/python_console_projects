# (Project: Two-Player, Two-Dimensional Tic-Tac-Toe) Write a script to play two- dimensional Tic-Tac-Toe between two human players who alternate entering their moves on the same computer. Use a 3-by-3 two-dimensional array. Each player indicates their moves by entering a pair of numbers representing the row and column indices of the square in which they want to place their mark, either an 'X' or an 'O'. When the first play- er moves, place an 'X' in the specified square. When the second player moves, place an 'O' in the specified square. Each move must be to an empty square. After each move, de- termine whether the game has been won and whether it’s a draw.


# SOLUTION NUMBER 1
import numpy as np

# check either player 1 won or nor
def player_1_won(arr):
        if np.all(arr[[0,0,0],[0,1,2]] == 'X') or np.all(arr[[1,1,1],[0,1,2]] == 'X') or np.all(arr[[2,2,2],[0,1,2]] == 'X') or np.all(arr[[0,1,2],[0,0,0]] == 'X') or np.all(arr[[0,1,2],[1,1,1]] == 'X') or np.all(arr[[0,1,2],[2,2,2]] == 'X') or np.all([[0,1,2],[0,1,2]] == 'X') or np.all(arr[[0,1,2],[2,1,0]] == 'X'):
            return True
        return False

# check either player 2 won or nor
def player_2_won(arr):
    if np.all(arr[[0,0,0],[0,1,2]] == 'O') or np.all(arr[[1,1,1],[0,1,2]] == 'O') or np.all(arr[[2,2,2],[0,1,2]] == 'O') or np.all(arr[[0,1,2],[0,0,0]] == 'O') or np.all(arr[[0,1,2],[1,1,1]] == 'O') or np.all(arr[[0,1,2],[2,2,2]] == 'O') or np.all([[0,1,2],[0,1,2]]) or np.all(arr[[0,1,2],[2,1,0]] == 'O'):
        return True
    return False

# check either game draw or not
def game_draw(arr):
    if not player_1_won(arr) and not player_2_won(arr) and np.all(arr != ''):
        return True
    return False

# board for the player where they play
def tic_tac_toe(arr):
    while True:
        while True:
            try:
                player_1_entry = input('player 1 move:')
                player_1_move = player_1_entry.split(' ')
                if arr[int(player_1_move[0]),int(player_1_move[1])] =='':
                    arr[int(player_1_move[0]),int(player_1_move[1])] = 'X'
                    print(arr)
                    break
                else:
                    print('wrong move!')
                    print('enter again')
                raise Exception
            except Exception as e:
                print(e)
        if player_1_won(arr):
            print('player 1 won!')
            break
        if game_draw(arr):
            print('game draw!')
            break
        while True:
            try:
                player_2_entry = input('player 2 move:')
                player_2_move = player_2_entry.split(' ')
                if arr[int(player_2_move[0]),int(player_2_move[1])] =='':
                    arr[int(player_2_move[0]),int(player_2_move[1])] = 'O'
                    print(arr)
                    break
                else:
                    print('wrong move!')
                    print('enter again')
                raise Exception
            except Exception as e:
                print(e)
        if player_2_won(arr):
            print('player 2 won!')
            break
arr = np.empty((3,3),str)


# SOLUTION NUMBER 2 improved version
import numpy as np

def player_won(arr,symbol):
    # check for column ,row and diagonals
    return (np.any(np.all(arr == symbol, axis = 0)) or # check for column
            np.any(np.all(arr == symbol, axis = 1)) or # check for row
            np.any(np.all(np.diag(arr) == symbol)) or # check for main diagonal
            np.any(np.all(np.diag(np.fliplr(arr)) == symbol))) # check for anti main diagonal

def draw(arr):
    # check for draw
    return not player_won(arr,'X') and not player_won(arr,'O') and np.all(arr != '')

def print_board(arr):
    # print a two d board
    for row in arr:
        print(' | '.join(row))
        print('-'*6)
# game Tic Tac Toe
def tic_tac_toe(arr):
    # this loop let the player permitted to play untill draw or announce winner 
    while True:
        
        # this for loop lets the player 1 and player 2 to do there move number by number
        for player,symbol in [(1,'X'),(2,'O')]:
            
            # this loop let the current player to do for their valid move
            while True:
                try:
                    print_board(arr)
                    entry = input(f'Player {player} move:')
                    move = list(map(int,entry.split()))
                    if arr[move[0],move[1]] == '':
                        arr[move[0],move[1]] = symbol
                        break
                    else:
                        print('Cell occupied! Try again')
                except (ValueError,IndexError):
                    print('Invalid index! Enter valid row and column indices(0-2) with space between them i.e 0 0')
            
            if player_won(arr,symbol):
                print_board(arr)
                print(f'Player {player} Won!')
                return
            if draw(arr):
                print_board(arr)
                print('Game draw!')
                return
arr = np.full((3,3),'')
tic_tac_toe(arr)
