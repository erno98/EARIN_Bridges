"""tutaj wszystko do kupy skleimy
a na razie cos tam se testuje
"""
# TODO: Save tree to file:
#       https://stackoverflow.com/questions/1047318/easiest-way-to-persist-a-data-structure-to-a-file-in-python

#tescior
from loadboard import load_map
from generate_tree import generate_tree_bfs, generate_tree_dfs, print_board

moves, brd = generate_tree_bfs(load_map("bridges7x7_1.txt"))
# moves, brd = generate_tree_dfs(load_map("bridges7x7_3.txt"))

print_board(brd.board)
print(brd.solved)
