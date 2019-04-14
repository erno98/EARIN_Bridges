"""Module tree

This module contains a simple Tree class

"""

class Tree():
    """Simple Tree class

    attributes:
        root (Tree.Node): the root of the tree
    """

    class Node():
        """Internal class for the tree node

        attributes:
            content: value stored in the Node
            children ([]): list of children of this node
            parent (Node): parent Node
        """

        content = None
        children = []
        parent = None

        def __init__(self, value, parent = None):
            self.content = value
            self.children = []
            self.parent = parent

        def add_child(self, value):
            """Method add_child

            Creates a new child and sets its attributes

            args:
                value: value to be stored inside the child
            
            returns:
                child (Node): the created child
            """
            child = Tree.Node(value)
            child.parent = self
            self.children.append(child)
            
            return child

    root = None
    def __init__(self, root_value):
        self.root = Tree.Node(root_value)