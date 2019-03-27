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