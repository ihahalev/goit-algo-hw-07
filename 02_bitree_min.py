from BST import Node, root
from AVL_tree import AVLNode, root as AVLroot
from BST_parent import NodeWP, root as WProot, search

def find_min_val(root:Node|AVLNode|NodeWP) -> int:
    current = root
    if isinstance(current, NodeWP):
        while current.parent and (current.parent.right == current or current.parent.left == current):
            current = current.parent
    while current.left:
        current = current.left
    return current.key

# Test for BST
print(root)
print(find_min_val(root))

# Test for AVL
print(AVLroot)
print(find_min_val(AVLroot))

# Test for BST with parent link
print(WProot)
print(find_min_val(WProot))

intermediate = search(WProot, 14)
print("Staring from node with key=14")
print(find_min_val(intermediate))