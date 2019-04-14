""" main project file

Used for loading puzzles from files and testing both the IDFS and A* algorithms,
to then save the results to files.

"""
import os
from loadboard import load_map
from time import process_time
from uninformed import iterative_dfs
from informed import a_star
import sys
from debug import print_board
from progress_bar import print_progress

class Result():
        def __init__(self, start_board = [[]],\
                idfs_time = 0, idfs_depth = 0, idfs_board = [[]], idfs_solved = False, idfs_nodes = 0,\
                        astar_time = 0, astar_board = [[]], astar_solved = False, astar_nodes = 0):
                self.start_board = start_board
                self.idfs_time = idfs_time
                self.idfs_depth = idfs_depth
                self.idfs_board = idfs_board
                self.idfs_solved = idfs_solved
                self.idfs_nodes = idfs_nodes
                self.astar_time = astar_time
                self.astar_board = astar_board
                self.astar_solved = astar_solved
                self.astar_nodes = astar_nodes


# Get all puzzle files from the puzzle directory
puzzle_directories = ["./puzzles_iter_5x5", "./puzzles_iter_7x7"]
puzzles = []
for puzzle_directory in puzzle_directories:
        for filename in os.listdir(puzzle_directory):
            if filename.endswith(".txt"):
                puzzles.append(puzzle_directory + "/" + filename)

# Progress bar
total_puzzles = len(puzzles)
i = 0
print_progress(i, total_puzzles, prefix="Puzzles solved")

# Test algorithms
results = []
for input_file in puzzles:
        start_board = load_map(input_file)
        # Uninformed
        time_start = process_time()
        node_i, depth, tree_i, visit_i = iterative_dfs(start_board)
        time_i = process_time() - time_start
        # Informed
        time_start = process_time()
        node_a, tree_a, visit_a = a_star(start_board)
        time_a = process_time() - time_start
        # Saving Results
        res = Result()
        res.start_board = start_board
        res.idfs_board = node_i.content.board
        res.idfs_depth = depth
        res.idfs_solved = node_i.content.solved
        res.idfs_time = time_i
        res.idfs_nodes = visit_i
        res.astar_board = node_a.content.board
        res.astar_solved = node_a.content.solved
        res.astar_time = time_a
        res.astar_nodes = visit_a
        results.append(res)
        # Update progress bar
        i += 1
        print_progress(i, total_puzzles, prefix="Puzzles solved")

# Sort the results by depth (no. of bridges)
results.sort(key = lambda res: res.idfs_depth)

# Redirect output to file:
sys.stdout = open("results.txt", "w")

# Print results
print("Puzzle files used:")
print(puzzles)
for res in results:
        print("---------------")
        print("Starting Board:")
        print_board(res.start_board)
        print("Final Board: IDFS")
        print_board(res.idfs_board)
        print("Final Board: A*")
        print_board(res.astar_board)
        print("Solved: IDFS - ", res.idfs_solved, " A* - ", res.astar_solved)
        print("Depth (no. of bridges): ", res.idfs_depth)
        print("Time: IDFS - ", res.idfs_time, "s A* - ", res.astar_time, "s")
        print("Nodes visited: IDFS - ", res.idfs_nodes, " A* - ", res.astar_nodes)

# Print table
sys.stdout = open("results_table.txt", "w")
print("Size\tDepth\tIDFS time\tA* time\tIDFS nodes\tA* nodes")
for res in results:
        print(len(res.start_board), "\t", res.idfs_depth, "\t", res.idfs_time, "\t", res.astar_time, "\t",
                res.idfs_nodes, "\t", res.astar_nodes, "\t")