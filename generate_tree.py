# TODO:
#  Progress bar: https://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console

from copy import deepcopy
from tree import Tree
from boardstate import BoardState
# from progress_bar import print_progress
from scipy.special import binom
from math import factorial as fact
from heuristic import board_mass
from debug import print_board

__debug = True

def generate_tree_bfs(board: [[]]):
    """
    """
    # Checking size
    size = len(board)
    for i in range(size):
        if len(board[i]) != size:
            raise Exception("Board matrix is not a square")
    # Creating BoardState from a matrix
    root_board = BoardState(board)
    root_board.generate_islands()
    root_board.evaluate()
    island_count = len(root_board.islands)

    max_bridges = root_board.possible_bridges()

    node_number = 1 + max_bridges
    for i in range(2, int(max_bridges)):
        node_number += fact(max_bridges) / fact(max_bridges-i)

    # Initiating Tree
    moves_tree = Tree(root_board)

    # Initiating stack
    to_generate = [moves_tree.root]
    nodes_visited = 0
    generated = 0
    final_board = None

  #  print_progress(0, node_number, prefix='Nodes visited', suffix='Complete')

    while len(to_generate) > 0:

        # Take element from stack
        node_current = to_generate.pop()
        nodes_visited += 1
      #  print_progress(nodes_visited, node_number, prefix='Nodes visited', suffix='Complete')
        board_next = deepcopy(node_current).content



        # Making all possible moves
        for i in range(island_count):
            for j in range(i + 1, island_count):



                # If bridge added succesfully, add to tree and stack and copy again
                if board_next.add_bridge(i, j):
                    board_next.evaluate()
                    # print(board_mass(board_next))
                    if moves_tree.find(board_next):
                        continue
                    generated += 1
                    if __debug:
                        print(generated)
                        print(board_next.solved)
                        print_board(board_next.board)
                    if board_next.solved:
                        print('\n')
                        print(generated)
                        print(board_next.solved)
                        final_board = board_next
                        print_board(board_next.board)
                        return moves_tree, final_board

                    node_next = Tree.Node(board_next)
                    node_current.children.append(node_next)
                    to_generate.insert(0, node_next)
                    board_next = deepcopy(node_current).content

    return moves_tree, final_board


generated_dfs = 0


def generate_tree_dfs(board: [[]]):
    """
    """
    # Checking size
    size = len(board)
    for i in range(size):
        if len(board[i]) != size:
            raise Exception("Board matrix is not a square")
    # Creating BoardState from a matrix
    root_board = BoardState(board)
    root_board.generate_islands()
    root_board.evaluate()

    # Initiating Tree
    moves_tree = Tree(root_board)

    node_current = moves_tree.root
    final_board = dfs_internal(node_current, moves_tree)

    return moves_tree, final_board


def dfs_internal(node: Tree.Node, tree: Tree):
    global generated_dfs
    island_count = len(node.content.islands)
    board_next = deepcopy(node).content

    for i in range(island_count):
            for j in range(i + 1, island_count):
                # If bridge added successfully, add to tree etc
                if board_next.add_bridge(i, j):
                    board_next.evaluate()
                    if tree.find(board_next):
                        continue
                    generated_dfs += 1
                    if __debug:
                        print(generated_dfs)
                        print(board_next.solved)
                        print_board(board_next.board)
                    if board_next.solved:
                        print("HALO")
                        return board_next
                    node_next = Tree.Node(board_next)
                    node.children.append(node_next)
                    final_board = dfs_internal(node_next, tree)
                    if final_board != None:
                        return final_board
    return None
