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
    def __init__(self, board_matrix = [[]], island_list = []):
        """init method

        By default the board matrix and island list are initialized as empty
        The solved attribute is always initialized as False, use method evaluate() to update
        """
        self.board = board_matrix
        self.islands = island_list
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
            