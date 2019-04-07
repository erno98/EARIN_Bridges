from tree import Tree
from boardstate import BoardState


def board_mass(board: BoardState):
    """Function for evaluating the mass of given board

    define bridge mass BM as:
        BM = i_n + i_k
        where i is the value of the island n and k consecutively, connected to each other
        REMARK: if i_n = 1, then i_k cannot be 1.

    args:
        BoardState object

    Returns:
        mass of the board
    """

    mass = 0

    for island in board.islands:
        for i in range(len(island.connections)):
            mass += island.connections[i] * (island.bridges_expected + board.islands[i].bridges_expected)

    return mass/2


def board_cohesion(board: BoardState):
    """Function for evaluating cohesion of given board
        cohesion describes how big island 'agglomerations' exist in the board.

        define board cohesion C as:
            C = n - x
            where n is the number of all islands, and x is the biggest number of islands forming a path

        args:
            BoardState object

        Returns:
            cohesion of the board (int)
    """

    islands_num = len(board.islands)

    path_lengths = []
    visited = []
    for i in range(islands_num):
        stack = []
        if visited.count(i) != 0:
            continue
        stack.append(i)
        length = 0
        while len(stack) > 0:
            length += 1
            current = stack.pop()
            visited.append(current)
            for cn in range(len(board.islands)):
                if board.islands[current].connections[cn] > 0:
                    if visited.count(cn) == 0 and stack.count(cn) == 0:
                        stack.append(cn)
        path_lengths.append(length)

    #TODO: zrobić to bo jestem zjebany

    cohesion = islands_num - max(path_lengths)
    return cohesion

