#Random tests for now
import boardstate as bs

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

print_board(board_m)

bstate = bs.BoardState(board_m)
bstate.generate_islands()

#Basic test boardstate
print("---")
print_board(bstate.board)
print("---")
for isl in bstate.islands:
    print(isl.bridges_expected)
print("---")
print(bstate.islands[0].x)
print(bstate.islands[0].y)
print(bstate.islands[0].connections)
print(len(bstate.islands[0].connections))
print("---")

#Add bridge test
for i in range(3):
    bstate.add_bridge(0, 1)
    print_board(bstate.board)
    print("---")
    print(bstate.islands[0].connections)
    print(bstate.islands[1].connections)
    print("---")

bstate.add_bridge(8, 12)
print_board(bstate.board)
print("---")
print(bstate.islands[8].connections)
print(bstate.islands[12].connections)
print("---")

bstate.add_bridge(9, 10)
print_board(bstate.board)
print("---")
print(bstate.islands[9].connections)
print(bstate.islands[10].connections)
print("---")

#Eval test
print(bstate.evaluate())
print("---")