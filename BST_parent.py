class NodeWP:
    def __init__(self, key, parent = None):
        self.left:NodeWP|None = None
        self.right:NodeWP|None = None
        self.parent:NodeWP|None = parent
        self.key = key

    def __str__(self, level=0, prefix="Root: "):
        ret = "\t" * level + prefix + str(self.key) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret

def insert_WP(root:NodeWP|None, key, parent:NodeWP|None = None):
    if root is None:
        return NodeWP(key, parent)
    else:
        if key < root.key:
            root.left = insert_WP(root.left, key, root)
        else:
            root.right = insert_WP(root.right, key, root)
    return root

def search(root:NodeWP|None, key):
    if root is None or root.key == key:
        return root
    if key < root.key:
        return search(root.left, key)
    return search(root.right, key)

root = NodeWP(5)
root = insert_WP(root, 3)
root = insert_WP(root, 2)
root = insert_WP(root, 4)
root = insert_WP(root, 10)
root = insert_WP(root, 15)
root = insert_WP(root, 14)
root = insert_WP(root, 12)
root = insert_WP(root, 7)
root = insert_WP(root, 1)
root = insert_WP(root, 6)
root = insert_WP(root, 8)
root = insert_WP(root, 9)