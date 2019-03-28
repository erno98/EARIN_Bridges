from tree import Tree
from boardstate import BoardState
from copy import deepcopy
#for testing
from random import randint

def a_star(board: [[]]):
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
    #TODO: insert objective function
    root_board.objective_function = 0
    island_count = len(root_board.islands)

    # Initiating Tree
    moves_tree = Tree(root_board)

    # Initiating stack
    to_visit = [moves_tree.root]
    nodes_visited = 0
    final_node = None

    while len(to_visit) > 0:

        # Take element from stack
        #TODO: take one with smallest objective function
        to_visit.sort(key = lambda node: node.content.objective_function, reverse = True)
        node_current = to_visit.pop()
        nodes_visited += 1

        node_current.content.evaluate()
        if node_current.content.solved:
            final_node = node_current
            return final_node, moves_tree, nodes_visited

        # Generate neighbors
        board_next = deepcopy(node_current).content
        # Making all possible moves
        for i in range(island_count):
            for j in range(i + 1, island_count):
                # If bridge added succesfully, add to tree and stack and copy again
                if board_next.add_bridge(i, j):
                    #TODO: insert objective function
                    board_next.objective_function = randint(0, 20)
                    child = node_current.add_child(board_next)
                    to_visit.append(child)
                    board_next = deepcopy(node_current).content

    return final_node, moves_tree, nodes_visited