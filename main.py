"""tutaj wszystko do kupy skleimy
a na razie cos tam se testuje
"""
# TODO: Save tree to file:
#       https://stackoverflow.com/questions/1047318/easiest-way-to-persist-a-data-structure-to-a-file-in-python

#tescior
from loadboard import load_map
from generate_tree import generate_tree_bfs, generate_tree_dfs
from debug import print_board
from uninformed import iterative_dfs

# moves, brd = generate_tree_bfs(load_map("bridges7x7_1.txt"))
# moves, brd = generate_tree_dfs(load_map("bridges7x7_3.txt"))

node, depth, tree = iterative_dfs(load_map("board-easy.txt"))
brd = node.content

print_board(brd.board)
print("Solved = ", brd.solved)
print("depth = ", depth)
