from BST import Node, root
from AVL_tree import AVLNode, root as AVLroot
from BST_parent import NodeWP, root as WProot, search

def preorder_traversal_sum(root:Node|AVLNode|None, top = False):
    if isinstance(root, NodeWP) and not top:
        while root.parent and (root.parent.right == root or root.parent.left == root):
            root = root.parent
        top = True
    if root:
        sum = root.key
        sum +=preorder_traversal_sum(root.left, top) or 0
        sum +=preorder_traversal_sum(root.right, top) or 0
        return sum

def inorder_traversal_sum(root:Node|AVLNode|None, top = False):
    if isinstance(root, NodeWP) and not top:
        while root.parent and (root.parent.right == root or root.parent.left == root):
            root = root.parent
        top = True
    if root:
        sum = 0
        sum += inorder_traversal_sum(root.left, top) or 0
        sum += root.key
        sum += inorder_traversal_sum(root.right, top) or 0
        return sum

def postorder_traversal_sum(root:Node|AVLNode|None, top = False):
    if isinstance(root, NodeWP) and not top:
        while root.parent and (root.parent.right == root or root.parent.left == root):
            root = root.parent
        top = True
    if root:
        sum = 0
        sum += postorder_traversal_sum(root.left, top) or 0
        sum += postorder_traversal_sum(root.right, top) or 0
        sum += root.key
        return sum

# Test for BST
print(root)
print(preorder_traversal_sum(root))
print(inorder_traversal_sum(root))
print(postorder_traversal_sum(root))

# Test for AVL
print(AVLroot)
print(preorder_traversal_sum(AVLroot))
print(inorder_traversal_sum(AVLroot))
print(postorder_traversal_sum(AVLroot))

# Test for BST with parent link
print(WProot)
print(preorder_traversal_sum(WProot))
print(inorder_traversal_sum(WProot))
print(postorder_traversal_sum(WProot))

intermediate = search(WProot, 14)
print("Staring from node with key=14")
print(preorder_traversal_sum(intermediate))
print(inorder_traversal_sum(intermediate))
print(postorder_traversal_sum(intermediate))
