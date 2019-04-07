from loadboard import load_map
from debug import print_board
from uninformed import iterative_dfs
from informed import a_star
from time import process_time

start_board = load_map("bridges7x7_3.txt")

# time_start = process_time()
# node_i, depth_i, tree_i, visited_i = iterative_dfs(start_board)
# time_i = process_time() - time_start

time_start = process_time()
node_a, tree_a, visited_a = a_star(start_board)
time_a = process_time() - time_start

# print("Solved - IDFS: ", node_i.content.solved, " A*: ", node_a.content.solved)
# print("Time - IDFS: ", time_i, "s A*: ", time_a, "s")
# print("Nodes visited - IDFS: ", visited_i, " A*: ", visited_a)
print("Solved - A*: ", node_a.content.solved)
print("Time - A*: ", time_a, "s")
print("Nodes visited - A*: ", visited_a)