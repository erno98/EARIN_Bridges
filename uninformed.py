from tree import Tree
from boardstate import BoardState
from copy import deepcopy

visited = 0

def iterative_dfs(board: [[]]):
    """
    """
    #Initializing boardstate
    # Checking size
    size = len(board)
    for i in range(size):
        if len(board[i]) != size:
            raise Exception("Board matrix is not a square")
    # Creating BoardState from a matrix
    root_board = BoardState(board)
    root_board.generate_islands()
    root_board.evaluate()

    #IDFS Algorithm
    global visited
    visited = 0
    depth = 0
    final_node = None
    while final_node == None:
        depth += 1
        final_node, final_tree = dfs(root_board, depth)
    return final_node, depth, final_tree, visited


def dfs(bstate: BoardState, depth_max: int):
    """
    """
    # Initiating Tree
    moves_tree = Tree(bstate)

    node_current = moves_tree.root
    final_board = dfs_internal(node_current, moves_tree, depth_max)
    return final_board, moves_tree

def dfs_internal(node: Tree.Node, tree: Tree, depth_max: int, depth = 0):
    if depth == depth_max:
        return None

    global visited
    visited += 1

    depth += 1
    
    island_count = len(node.content.islands)
    board_next = deepcopy(node).content

    for i in range(island_count):
            for j in range(i + 1, island_count):
                # If bridge added successfully, add to tree etc
                if board_next.add_bridge(i, j):
                    board_next.evaluate()
                    if board_next.solved:
                        result = node.add_child(board_next)
                        return result
                    node_next = node.add_child(board_next)
                    result = dfs_internal(node_next, tree, depth_max, depth)
                    if result != None:
                        return result
                    board_next = deepcopy(node).content
    return None