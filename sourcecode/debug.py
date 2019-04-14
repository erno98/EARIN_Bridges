"""Module debug

This module contains only a function for printing the board, which was used for debuging,
but it is also now used to print the results into a file

"""

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