"""Module boardstate

This module is supposed to represent the board state that will be inserted into a tree as a class.

Todo:
    * wszystko iksde
    * nwm czy klasa Island powinna być w środku BoardState czy osobno
"""

class BoardState():
    """Class representing the board state

    Attributes:
        board ([[]]): a 2D array representing the board
        islands ([]): a list of Island classes, representing islands
        solved (bool): denotes whether the board represents a solved state or not
    """
    def __init__(self, board_matrix = [[]]):
        """init method

        By default the board matrix is initialized as empty
        The island list is always initialized as empty, use method generate_islands() to update
        The solved attribute is always initialized as False, use method evaluate() to update
        """
        self.board = board_matrix
        self.islands = []
        self.solved = False

    def evaluate(self):
        """Method for evaluating if the board state represented is solved or not

        Updates the solved parameter and also returns its value

        args:
            None

        Returns:
            True if board is solved, False otherwise

        TODO:
            Write the function lol
        """
        self.solved = False
        return False

    def add_island(self, x: int, y: int, bridges: int):
        """Method for adding a new island to the lsit of islands

        It creates an instance of class Island with the given parameters, appends it to the island list
        and adds a new island to the connections list of all islands on the list

        args:
            x (int): x coordinate
            y (int): y coordinate
            bridges (int): number of expected bridges

        returns:
            void
        """
        self.islands.append(BoardState.Island(x, y, bridges))
        for isl in self.islands:
            isl.connections.append(0)

    def generate_islands(self):
        """Method for generating the island list from the current board matrix

        args:
            None

        returns:
            void
        """
        pass

    class Island():
        """Class representing one island, used in the island list

        Attributes:
            x (int): x coordinate
            y (int): y coordinate
            bridges_expected (int): the expected number of bridges connected to this island
            bridges_current (int): the current number of bridges connected to this island
            connections ([]): a list of connections to other islands,
                            lists all islands and takes values 0, 1, 2 - number of bridges connecting them
        """
        def __init__(self, x: int, y: int, bridges: int):
            self.x = x
            self.y = y
            self.bridges_expected = bridges
            self.bridges_current = 0
            self.connections = []
            