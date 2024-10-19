import os 
from random import choice


def init_board():
    """Returns an empty 3-by-3 board (with .)."""
    board = [['.', '.', '.', ],
             ['.', '.', '.', ],
             ['.', '.', '.', ]]
    return board


def print_board(board):
    row_col_names = {0: "A", 1: "B", 2: "C"}
    print()
    print("1    2   3\n".center(35))
    for row, col in enumerate(board):
        print(f"{row_col_names[row]}     {col[0]}  |  {col[1]} |  {col[2]}".center(30))
        if row <= 1:
            print("----+----+----".center(35))
    print()


def get_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    column_id = {"A": 0, "B": 1, "C": 2}
    valid_moves = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
    user_wants_to_quit = False
    while not user_wants_to_quit:
        user_input = input(f"Player: {player} - choose your move: ").upper()
        if user_input == "QUIT":
            user_wants_to_quit = True
        elif user_input not in valid_moves:
            print(f" {user_input} - Not a valid move. Try again!")
        else:
            row, col = column_id[user_input[0]], int(user_input[1]) - 1
            if user_input in valid_moves and board[row][col] == '.':
                return row, col
            else:
                print(f" {user_input} - Cell already taken! Try again!")


    

def mark(board, player, row, col):
    """Marks the element at row & col on the board for player."""
    if board[row][col] == '.':
        board[row][col] = player
    return True


def has_won(board, player):
    """Returns True if player has won the game."""
    win_boards = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
        [board[0][0], board[1][1], board[2][2]]
    ]
    return True if [player, player, player] in win_boards else False



def is_full(board):
    """Returns True if board is full."""
    for col in board:
        if '.' in col:
            return False
    return True


def print_result(winner, board):
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    if has_won(board=board, player=winner):
        print(f"{winner} has won!")
    elif is_full(board):
        print("It's a tie!")

def empty_cells(board: list):
    """
    Checks empty cells on board and returns list of available coordinates
    """
    empty_cells = [[r, c] for r, row in enumerate(board) for c, cell in enumerate(row) if cell == "."]
    return empty_cells

def change_player(player: str):
    """ Switches a player """
    if player == player_0:
        return player_X
    else:
        return player_0 

def evaluate_end_game(board: list) :
    """
    Returns game state as int
    """
    if has_won(board=board, player=player_X):
        return -1
    elif has_won(board=board, player=player_0):
        return 1
    elif is_full(board=board):
        return 0

def game_menu():   
    levels = ['1', '2']
    while True:
        mode = input('''\nChoose your game mode 
        1 - HUMAN HUMAN
        2 - HUMAN vs AI 
        QUIT
        ''')

        if mode in levels:
            return mode
        else:
            print('Provide valid level.')      
    

def tictactoe_game(mode='HUMAN-HUMAN'):
    board = init_board()
    print_board(board=board)
    player_turn = player_X
    user_wants_to_quit = False
    move = True
    while evaluate_end_game(board) is None and not user_wants_to_quit:
        if mode == 'HUMAN-HUMAN':
            move = get_move(board=board, player=player_turn)
        elif mode == 'HUMAN-AI':
            if player_turn == player_X:
                move = get_move(board=board, player=player_turn)
            

        if move is not None:
            mark(board=board, player=player_turn, row=move[0], col=move[1])
            print_board(board=board)
            if evaluate_end_game(board=board) is None:
                player_turn = change_player(player=player_turn)
        else:
            user_wants_to_quit = True
    if not user_wants_to_quit:
        print_result(board=board, winner=player_turn)
        user_input = input("Play again (y/n): ").upper()
        if user_input == "Y":
            main_menu()
        else:
            user_wants_to_quit = True

def main_menu():
    print("Welcome to Tic-Tac-Toe game!")
    print('''\nGame Rules:
    Each player is supposed to pick the proper field. The options varies from 1a to 3c.
    You will see the board printed before the first move.
    To pick the field you should insert for example \"1a\" or \"a1\" or \"1A\" or \"1A.
    The result of example above is the same but all of these inputs are valid.
    If you pick wrong field, you will have another chances to insert proper one.\n
    Have fun!''')
    print_board(board=init_board())
    user_wants_to_quit = False
    user_input = input("Choose game mode:\n\n1. HUMAN-HUMAN\n2. HUMAN-AI\n").upper()
    valid_input = ["1", "2", "QUIT"]

    while user_input not in valid_input and not user_wants_to_quit:
        user_input = input("Invalid choice. Try again!: ").upper()
    if user_input == "QUIT":
        user_wants_to_quit = True
    if user_input == "1":
        tictactoe_game(mode="HUMAN-HUMAN")
    if user_input == "2":
        tictactoe_game(mode="HUMAN-AI")
    print("\n")

if __name__ == '__main__':
    player_X = "X"
    player_0 = "0"
    main_menu()