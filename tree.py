class Tree():
    class Node():
        content = None
        children = []

        def __init__(self, value):
            self.content = value
            self.children = []

    root = None
    def __init__(self, root_value):
        self.root = Tree.Node(root_value)