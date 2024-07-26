class Node:
    def __init__(self, key):
        self.left:Node|None = None
        self.right:Node|None = None
        self.key = key

    def __str__(self, level=0, prefix="Root: "):
        ret = "\t" * level + prefix + str(self.key) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret

def insert(root:Node|None, key):
    if root is None:
        return Node(key)
    else:
        if key < root.key:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

root = Node(5)
root = insert(root, 3)
root = insert(root, 2)
root = insert(root, 4)
root = insert(root, 10)
root = insert(root, 15)
root = insert(root, 14)
root = insert(root, 12)
root = insert(root, 7)
root = insert(root, 1)
root = insert(root, 6)
root = insert(root, 8)
root = insert(root, 9)