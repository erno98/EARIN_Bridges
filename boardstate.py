"""Module boardstate

This module is supposed to represent the board state that will be inserted into a tree as a class.

Todo:
    * real tests
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

    def possible_bridges(self):
        """Method for evaluating maximal number of possible bridges

        args:
            None

        Returns:
            number of bridges possible to be placed
        """

        num = 0

        for isl in self.islands:
            num += isl.bridges_expected

        return num/2


    def evaluate(self):
        """Method for evaluating if the board state represented is solved or not

        Updates the solved parameter and also returns its value

        args:
            None

        Returns:
            True if board is solved, False otherwise
        """
        #To be solved:
        #A all islands full
        #B all islands connected
        for isl in self.islands:
            if isl.bridges_current != isl.bridges_expected:
                self.solved = False
                return False

        visited = []
        stack = []
        stack.append(0)
        while len(stack) > 0:
            current = stack.pop()
            visited.append(current)
            for cn in range(len(self.islands)):
                if self.islands[current].connections[cn] > 0:
                    if visited.count(cn) == 0 and stack.count(cn) == 0:
                        stack.append(cn)

        if len(visited) == len(self.islands):
            self.solved = True
            return True

        self.solved = False
        return False

    def add_island(self, x: int, y: int, bridges: int):
        """Method for adding a new island to the list of islands

        It creates an instance of class Island with the given parameters, appends it to the island list
        and adds a new island to the connections list of all islands on the list

        args:
            x (int): x coordinate
            y (int): y coordinate
            bridges (int): number of expected bridges

        returns:
            void
        """
        new_isl = BoardState.Island(x, y, bridges)
        for isl in self.islands:
            new_isl.connections.append(0)
        self.islands.append(new_isl)
        for isl in self.islands:
            isl.connections.append(0)

    def generate_islands(self):
        """Method for generating the island list from the current board matrix

        args:
            None

        returns:
            void
        """
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] > 0:
                    self.add_island(i, j, self.board[i][j])

    def add_bridge(self, island_one: int, island_two: int):
        """Method for adding a new bridge between two specified islands.
        Only places bridges if it is a correct move
        
        args:
            island_one (int): id (index in the list) of the first island two connect
            island_two (int): id of the other island to connect

        returns:
            True if placement was successful, False otherwise
        """
        #Reasons to fail:
        #A Island IDs are incorrect
        #B One of the islands is full
        #C Islands already connected twice
        #D Islands not on the same x or y
        #E Bridge or island in the way
        #If bridges are already connected once, E can be skipped

        #A
        if island_one < 0 or island_two < 0 or\
            island_one > len(self.islands) or island_two > len(self.islands) or\
                island_one == island_two:
            
            return False

        #B
        if self.islands[island_one].bridges_expected == self.islands[island_one].bridges_current or\
            self.islands[island_two].bridges_expected == self.islands[island_two].bridges_current:

            return False

        #C
        if self.islands[island_one].connections[island_two] == 2:

            return False

        #D
        if self.islands[island_one].x != self.islands[island_two].x and\
            self.islands[island_one].y != self.islands[island_two].y:

            return False

        #E
        if self.islands[island_one].connections[island_two] != 1:
            if self.islands[island_one].x == self.islands[island_two].x:
                x = self.islands[island_one].x
                #Horizontal bridge
                for y in range(self.islands[island_one].y + 1, self.islands[island_two].y):
                    if self.board[x][y] > 0:
                        return False
            elif self.islands[island_one].y == self.islands[island_two].y:
                y = self.islands[island_one].y
                #Vertical bridge
                for x in range(self.islands[island_one].x + 1, self.islands[island_two].x):
                    if self.board[x][y] > 0:
                        return False

        #Otherwise:
        #Increasing connections
        self.islands[island_one].connections[island_two] += 1
        self.islands[island_two].connections[island_one] += 1
        self.islands[island_one].bridges_current += 1
        self.islands[island_two].bridges_current += 1
        #Selecting and placing bridge
        bridge = 0
        if self.islands[island_one].x == self.islands[island_two].x:
            x = self.islands[island_one].x
            #Horizontal bridge
            if self.islands[island_one].connections[island_two] == 2:
                #Double bridge
                bridge = 22
            if self.islands[island_one].connections[island_two] == 1:
                #Single bridge
                bridge = 21
            for y in range(self.islands[island_one].y + 1, self.islands[island_two].y):
                self.board[x][y] = bridge
        elif self.islands[island_one].y == self.islands[island_two].y:
            y = self.islands[island_one].y
            #Vertical bridge
            if self.islands[island_one].connections[island_two] == 2:
                #Double bridge
                bridge = 12
            if self.islands[island_one].connections[island_two] == 1:
                #Single bridge
                bridge = 11
            for x in range(self.islands[island_one].x + 1, self.islands[island_two].x):
                self.board[x][y] = bridge
        #Done
        return True

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
        #
        # def is_connected(self):
        #     return self.connections != []

