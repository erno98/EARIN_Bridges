from copy import deepcopy
from tree import Tree
from boardstate import BoardState

def generate_tree(board: [[]]):
    """
    """
    #Checking size
    size = len(board)
    for i in range(size):
        if len(board[i]) != size:
            raise Exception("Board matrix is not a square")
    #Creating BoardState from a matrix
    root_board = BoardState(board)
    root_board.generate_islands()
    root_board.evaluate()
    island_count = len(root_board.islands)

    #Initiating Tree
    moves_tree = Tree(root_board)

    #Initiating stack
    to_generate = []
    to_generate.append(moves_tree.root)
    nodes_visited = 0
    while len(to_generate) > 0:
        #Take element from stack
        node_current = to_generate.pop()
        nodes_visited += 1
        board_next = deepcopy(node_current).content
        #Making all possible moves
        for i in range(island_count):
            for j in range(i + 1, island_count):
                #If bridge added succesfully, add to tree and stack and copy again
                if board_next.add_bridge(i, j):
                    node_next = Tree.Node(board_next)
                    node_current.children.append(node_next)
                    to_generate.append(node_next)
                    board_next = deepcopy(node_current).content

    return moves_tree