#Hardcoded solve
from boardstate import BoardState

def print_board(brd: [[]]):
    for m in brd:
        row = ""
        for n in m:
            if n == 21:
                row = row+"-"+" "
            elif n == 22:
                row = row+"="+" "
            elif n == 11:
                row = row+"|"+" "
            elif n == 12:
                row = row+":"+" "
            else:
                row = row+str(n)+" "
        print(row)

board_m = [[3, 0, 0, 0, 0, 2, 0],\
    [0, 3, 0, 2, 0, 0, 0],\
    [4, 0, 2, 0, 0, 4, 0],\
    [0, 0, 0, 0, 0, 0, 0],\
    [0, 0, 3, 0, 2, 0, 0],\
    [0, 2, 0, 0, 0, 3, 0],\
    [3, 0, 0, 0, 2, 0, 1]]

bstate = BoardState(board_m)
bstate.generate_islands()

print_board(bstate.board)
print(bstate.evaluate())
print("---")

bstate.add_bridge(0, 1)
bstate.add_bridge(2, 3)
bstate.add_bridge(2, 3)
bstate.add_bridge(5, 6)
bstate.add_bridge(7, 8)
bstate.add_bridge(7, 8)
bstate.add_bridge(9, 10)
bstate.add_bridge(11, 12)
bstate.add_bridge(12, 13)
bstate.add_bridge(0, 4)
bstate.add_bridge(0, 4)
bstate.add_bridge(4, 11)
bstate.add_bridge(4, 11)
bstate.add_bridge(1, 6)
bstate.add_bridge(2, 9)
bstate.add_bridge(6, 10)
bstate.add_bridge(6, 10)
bstate.add_bridge(5, 7)

print_board(bstate.board)
print(bstate.evaluate())
print("---")
