from copy import deepcopy
from tree import Tree
from boardstate import BoardState
__debug = True

if __debug:
    def print_board(brd: [[]]):
        for m in brd:
            row = ""
            for n in m:
                if n == 21:
                    row = row+"-"+" "
                elif n == 22:
                    row = row+"="+" "
                elif n == 11:
                    row = row+"|"+" "
                elif n == 12:
                    row = row+":"+" "
                else:
                    row = row+str(n)+" "
            print(row)

def generate_tree_bfs(board: [[]]):
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
    generated = 0
    final_board = None
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
                    board_next.evaluate()
                    if moves_tree.find(board_next):
                        continue
                    generated += 1
                    if __debug:
                        print(generated)
                        print(board_next.solved)
                        print_board(board_next.board)
                    if board_next.solved:
                        final_board = board_next
                        break
                    node_next = Tree.Node(board_next)
                    node_current.children.append(node_next)
                    to_generate.insert(0, node_next)
                    board_next = deepcopy(node_current).content

    return moves_tree, final_board

generated_dfs = 0

def generate_tree_dfs(board: [[]]):
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

    #Initiating Tree
    moves_tree = Tree(root_board)

    node_current = moves_tree.root
    dfs_internal(node_current, moves_tree)

    return moves_tree

def dfs_internal(node: Tree.Node, tree: Tree):
    global generated_dfs
    island_count = len(node.content.islands)
    board_next = deepcopy(node).content
    for i in range(island_count):
            for j in range(i + 1, island_count):
                #If bridge added succesfully, add to tree etc
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
                        return
                    node_next = Tree.Node(board_next)
                    node.children.append(node_next)
                    dfs_internal(node_next, tree)