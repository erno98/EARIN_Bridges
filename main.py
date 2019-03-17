"""tutaj wszystko do kupy skleimy
a na razie cos tam se testuje
"""
import boardstate as bs

def print_board(brd: [[]]):
    for m in brd:
        row = ""
        for n in m:
            row = row+str(n)+" "
        print(row)

board_m = [[3, 0, 0, 0, 0, 2, 0],\
    [0, 3, 0, 2, 0, 0, 0],\
    [4, 0, 2, 0, 0, 4, 0],\
    [0, 0, 0, 0, 0, 0, 0],\
    [0, 0, 3, 0, 2, 0, 0],\
    [0, 2, 0, 0, 0, 3, 0],\
    [3, 0, 0, 0, 2, 0, 1]]

print_board(board_m)

bstate = bs.BoardState(board_m)

print("---")
print_board(bstate.board)