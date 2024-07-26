class AVLNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left:AVLNode|None = None
        self.right:AVLNode|None = None

    def __str__(self, level=0, prefix="Root: "):
        ret = "\t" * level + prefix + str(self.key) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret

def get_height(node:AVLNode|None):
    if not node:
        return 0
    return node.height

def get_balance(node:AVLNode|None):
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)

def left_rotate(z:AVLNode) -> AVLNode|None:
    y = z.right
    T2 = y.left

    y.left = z
    z.right = T2

    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    return y

def right_rotate(y:AVLNode) -> AVLNode|None:
    x = y.left
    T3 = x.right

    x.right = y
    y.left = T3

    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))

    return x

def min_value_node(node:AVLNode) -> AVLNode:
    current = node
    while current.left:
        current = current.left
    return current

def insert_AVL(root:AVLNode|None, key):
    if not root:
        return AVLNode(key)

    if key < root.key:
        root.left = insert_AVL(root.left, key)
    elif key > root.key:
        root.right = insert_AVL(root.right, key)
    else:
        return root

    root.height = 1 + max(get_height(root.left), get_height(root.right))

    balance = get_balance(root)

    if balance > 1:
        if key < root.left.key:
            return right_rotate(root)
        else:
            root.left = left_rotate(root.left)
            return right_rotate(root)

    if balance < -1:
        if key > root.right.key:
            return left_rotate(root)
        else:
            root.right = right_rotate(root.right)
            return left_rotate(root)

    return root

root = AVLNode(5)
root = insert_AVL(root, 3)
root = insert_AVL(root, 2)
root = insert_AVL(root, 4)
root = insert_AVL(root, 10)
root = insert_AVL(root, 15)
root = insert_AVL(root, 14)
root = insert_AVL(root, 12)
root = insert_AVL(root, 7)
root = insert_AVL(root, 1)
root = insert_AVL(root, 6)
root = insert_AVL(root, 8)
root = insert_AVL(root, 9)