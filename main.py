"""tutaj wszystko do kupy skleimy
a na razie cos tam se testuje
"""
#tescior
from loadboard import load_map
from generate_tree import generate_tree_bfs

moves, brd = generate_tree_bfs(load_map("bridges7x7_1.txt"))

print("siema")