
class Node:
    def __init__(self, value):
        self. value = value
        self.left = None
        self.right = None


class Bintree:
    def __init__(self):
        self.root = None

    def put(self, new_value):
        # Sorterar in newvalue i trädet
        if self.root is None:
            self.root = Node(new_value)
        else:
            putta(self.root, new_value)

    def __contains__(self, value):
        # True om value finns i trädet, False annars
        return finns(self.root, value)

    def write(self):
        # Skriver ut trädet i inorder
        skriv(self.root)
        print("\n")


def putta(p, new_value):
    if new_value < p.value:
        if p.left is None:
            p.left = Node(new_value)
        else:
            putta(p.left, new_value)
    if new_value > p.value:
        if p.right is None:
            p.right = Node(new_value)
        else:
            putta(p.right, new_value)


def finns(p, value):
    if p is None:
        return False
    if value == p.value:
        return True
    if value < p.value:
        return finns(p.left, value)
    if value > p.value:
        return finns(p.right, value)


def skriv(p):
    if p is not None:
        skriv(p.left)
        print(p.value)
        skriv(p.right)
