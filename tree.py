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

    def __find_in_tree(self, what, where):
        if len(where.children) == 0:
            if where.content == what:
                return True
            else:
                return False
        for c in where.children:
            if self.__find_in_tree(what, c):
                return True
        return False

    def find(self, what):
        return self.__find_in_tree(what, self.root)