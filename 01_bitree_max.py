from BST import Node, root
from AVL_tree import AVLNode, root as AVLroot
from BST_parent import NodeWP, root as WProot, search

def find_max_val(root:Node|AVLNode|NodeWP) -> int:
    current = root
    if isinstance(current, NodeWP):
        while current.parent and (current.parent.right == current or current.parent.left == current):
            current = current.parent
    while current.right:
        current = current.right
    return current.key

# Test for BST
print(root)
print(find_max_val(root))

# Test for AVL
print(AVLroot)
print(find_max_val(AVLroot))

# Test for BST with parent link
print(WProot)
print(find_max_val(WProot))

intermediate = search(WProot, 4)
print("Staring from node with key=4")
print(find_max_val(intermediate))