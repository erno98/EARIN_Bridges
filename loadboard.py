
def load_map(file_name):

    with open(file_name, 'r') as file:
        return [list(map(int, row.strip('\n').split(' '))) for row in file]
    # for each row:
    #   - remove the '\n' symbol
    #   - split each element separated by ' '
    #   - map inside elements to integers