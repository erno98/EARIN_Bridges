class Tree():
    class Node():
        content = None
        children = []
        parent = None

        def __init__(self, value, parent = None):
            self.content = value
            self.children = []
            self.parent = parent

        def add_child(self, value):
                child = Tree.Node(value)
                child.parent = self
                self.children.append(child)
                
                return child

    root = None
    def __init__(self, root_value):
        self.root = Tree.Node(root_value)