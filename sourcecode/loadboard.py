"""Module loadboard

This module contains a function for loading a board from a text file
and storing it in a matrix (list of lists)

"""

def load_map(file_name):

    with open(file_name, 'r') as file:
        return [list(map(int, row.strip('\n').split(' '))) for row in file]
    # for each row:
    #   - remove the '\n' symbol
    #   - split each element separated by ' '
    #   - map inside elements to integers