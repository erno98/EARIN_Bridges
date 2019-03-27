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