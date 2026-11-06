# Josue Rosas 
# Student ID: 877784637 
# Section: 08
# Module 9 Assignment 3
def print_board(board):
    line = "-" * (2 * len(board[0]) + 1)
    for row in board:
        print(line)
        print("|" + "|".join(row) + "|")
    print(line)
board1_list = [['*','*','*'],
               ['*','+','*'],
               ['*','*','*']]
print_board(board1_list)
print() #just for a spacer line
board2_list = [['*',' ',' ','*'],
               ['*',' ',' ','*'],
               ['*',' ',' ','*'],
               ['*',' ',' ','*']]
print_board(board2_list)
print() #just for a spacer line
board3_list = [['*',' ','*',' ','*'],
               [' ','*',' ','*',' '],
               [' ',' ',' ',' ',' '],
               [' ','+',' ','+',' '],
               ['+',' ','+',' ','+']]
print_board(board3_list)